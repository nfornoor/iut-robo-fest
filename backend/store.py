from datetime import datetime

from models.device import Device, DeviceType, Room
from models.alert import Alert

devices: list[Device] = []
alerts: list[Alert] = []


def _device_id(room: Room, dtype: DeviceType, num: int) -> str:
    return f"{room.value}-{dtype.value}-{num}"


def _device_label(dtype: DeviceType, room: Room, num: int) -> str:
    room_labels = {Room.drawing: "Drawing Room", Room.work1: "Work Room 1", Room.work2: "Work Room 2"}
    type_labels = {DeviceType.fan: "Fan", DeviceType.light: "Light"}
    return f"{type_labels[dtype]} {num} ({room_labels[room]})"


def initialize_devices() -> list[Device]:
    global devices
    now = datetime.now()
    devices.clear()

    for room in Room:
        for i in range(1, 3):
            devices.append(Device(
                id=_device_id(room, DeviceType.fan, i),
                type=DeviceType.fan,
                room=room,
                label=_device_label(DeviceType.fan, room, i),
                rated_power_w=60,
                current_power_w=0,
                last_changed=now,
            ))
        for i in range(1, 4):
            devices.append(Device(
                id=_device_id(room, DeviceType.light, i),
                type=DeviceType.light,
                room=room,
                label=_device_label(DeviceType.light, room, i),
                rated_power_w=15,
                current_power_w=0,
                last_changed=now,
            ))

    return devices


def get_device(device_id: str) -> Device | None:
    return next((d for d in devices if d.id == device_id), None)


def get_devices_by_room(room: Room) -> list[Device]:
    return [d for d in devices if d.room == room]


def toggle_device(device_id: str) -> Device | None:
    device = get_device(device_id)
    if device is None:
        return None

    device.is_on = not device.is_on
    device.current_power_w = device.rated_power_w if device.is_on else 0
    device.last_changed = datetime.now()
    device.on_since = device.last_changed if device.is_on else None

    return device
