from datetime import datetime

from config import settings
from models.alert import Alert, AlertType
from models.device import Device, Room
from store import alerts


def _rooms_with_devices_on(devices: list[Device]) -> set[Room]:
    return {d.room for d in devices if d.is_on}


def check_after_hours(devices: list[Device], now: datetime | None = None) -> set[Room]:
    now = now or datetime.now()
    hour = now.hour
    start = settings.alert_after_hours_start
    end = settings.alert_after_hours_end

    if start <= hour < end:
        return set()

    return _rooms_with_devices_on(devices)


def check_continuous_on(devices: list[Device], now: datetime | None = None) -> set[Room]:
    now = now or datetime.now()
    threshold = settings.continuous_on_threshold_hours
    triggered: set[Room] = set()

    for room in Room:
        room_devices = [d for d in devices if d.room == room]
        if len(room_devices) == 0:
            continue

        all_on = all(d.is_on for d in room_devices)
        if not all_on:
            continue

        oldest = min(
            (d.on_since for d in room_devices if d.on_since is not None),
            default=None,
        )
        if oldest is None:
            continue

        hours_on = (now - oldest).total_seconds() / 3600
        if hours_on > threshold:
            triggered.add(room)

    return triggered


def _alert_key(alert_type: AlertType, room: str) -> str:
    return f"{alert_type.value}:{room}"


def update_alerts(devices: list[Device], now: datetime | None = None) -> list[Alert]:
    now = now or datetime.now()
    new_alerts: list[Alert] = []

    after_hours_rooms = check_after_hours(devices, now)
    continuous_on_rooms = check_continuous_on(devices, now)

    active_rooms: dict[str, set[str]] = {
        AlertType.after_hours.value: {r.value for r in after_hours_rooms},
        AlertType.continuous_on.value: {r.value for r in continuous_on_rooms},
    }

    existing_active: dict[str, Alert] = {}
    for alert in alerts:
        if alert.active:
            key = _alert_key(alert.type, alert.room)
            existing_active[key] = alert

    alert_counter = len(alerts) + 1

    for alert_type_str, rooms in active_rooms.items():
        alert_type = AlertType(alert_type_str)
        for room in rooms:
            key = _alert_key(alert_type, room)
            if key in existing_active:
                del existing_active[key]
            else:
                messages = {
                    AlertType.after_hours: f"Devices in {room} are on after office hours.",
                    AlertType.continuous_on: f"{room} has been fully on for over {settings.continuous_on_threshold_hours:.0f} hours.",
                }
                alert = Alert(
                    id=f"alert-{alert_counter:03d}",
                    type=alert_type,
                    room=room,
                    message=messages[alert_type],
                    triggered_at=now,
                    active=True,
                )
                alerts.append(alert)
                new_alerts.append(alert)
                alert_counter += 1

    for alert in existing_active.values():
        alert.active = False

    return new_alerts
