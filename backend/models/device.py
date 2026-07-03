from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class DeviceType(str, Enum):
    fan = "fan"
    light = "light"


class Room(str, Enum):
    drawing = "drawing"
    work1 = "work1"
    work2 = "work2"


class Device(BaseModel):
    id: str = Field(examples=["work1-fan-1"])
    type: DeviceType = Field(examples=["fan"])
    room: Room = Field(examples=["work1"])
    label: str = Field(examples=["Fan 1 (Work Room 1)"])
    is_on: bool = False
    rated_power_w: int = Field(examples=[60])
    current_power_w: int = 0
    total_energy_kwh_today: float = 0.0
    last_changed: datetime = Field(default_factory=datetime.now)
    on_since: datetime | None = None
