from fastapi import APIRouter, HTTPException

from models.alert import Alert
from models.device import Device, Room
from models.schemas import UsageResponse
from store import alerts, devices, get_device, get_devices_by_room, toggle_device as store_toggle

router = APIRouter()


@router.get("/devices")
def list_devices():
    """All 15 devices with current state."""
    return [d.model_dump(mode="json") for d in devices]


@router.get("/rooms/{room}")
def get_room(room: str):
    """Devices in a room: `drawing`, `work1`, or `work2`."""
    try:
        room_enum = Room(room)
    except ValueError:
        raise HTTPException(status_code=404, detail=f"Room '{room}' not found")
    room_devices = get_devices_by_room(room_enum)
    return [d.model_dump(mode="json") for d in room_devices]


@router.get("/usage")
def get_usage():
    """Current power draw (W) and accumulated energy (kWh) — total + per-room."""
    total_watts = sum(d.current_power_w for d in devices)
    total_kwh = sum(d.total_energy_kwh_today for d in devices)
    per_room = {}
    for room in Room:
        room_devices = [d for d in devices if d.room == room]
        per_room[room.value] = {
            "watts_now": sum(d.current_power_w for d in room_devices),
            "kwh_today": sum(d.total_energy_kwh_today for d in room_devices),
        }
    return UsageResponse(
        total_watts_now=total_watts,
        total_kwh_today=total_kwh,
        per_room=per_room,
    )


@router.get("/alerts")
def list_alerts():
    """Active alerts only."""
    return [a.model_dump(mode="json") for a in alerts if a.active]


@router.post("/devices/{device_id}/toggle")
def toggle_device(device_id: str):
    """Flip a device on/off. Use device IDs like `drawing-fan-1` or `work2-light-3`."""
    device = store_toggle(device_id)
    if device is None:
        raise HTTPException(status_code=404, detail=f"Device '{device_id}' not found")
    return device.model_dump(mode="json")
