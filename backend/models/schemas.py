from pydantic import BaseModel


class UsageResponse(BaseModel):
    total_watts_now: float
    total_kwh_today: float
    per_room: dict[str, dict[str, float]]


class WSMessage(BaseModel):
    type: str = "state_update"
    devices: list[dict]
    usage: UsageResponse
    alerts: list[dict]
