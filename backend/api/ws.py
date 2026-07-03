from fastapi import WebSocket

from models.device import Room
from models.schemas import UsageResponse
from store import alerts, devices

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        stale = []
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception:
                stale.append(connection)
        for conn in stale:
            self.active_connections.remove(conn)

    async def broadcast_state(self):
        total_watts = sum(d.current_power_w for d in devices)
        total_kwh = sum(d.total_energy_kwh_today for d in devices)
        per_room = {}
        for room in Room:
            room_devices = [d for d in devices if d.room == room]
            per_room[room.value] = {
                "watts_now": sum(d.current_power_w for d in room_devices),
                "kwh_today": sum(d.total_energy_kwh_today for d in room_devices),
            }

        message = {
            "type": "state_update",
            "devices": [d.model_dump(mode="json") for d in devices],
            "usage": UsageResponse(
                total_watts_now=total_watts,
                total_kwh_today=total_kwh,
                per_room=per_room,
            ).model_dump(mode="json"),
            "alerts": [a.model_dump(mode="json") for a in alerts if a.active],
        }

        await self.broadcast(message)


manager = ConnectionManager()
