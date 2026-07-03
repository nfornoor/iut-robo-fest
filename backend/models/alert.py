from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class AlertType(str, Enum):
    after_hours = "after_hours"
    continuous_on = "continuous_on"


class Alert(BaseModel):
    id: str = Field(examples=["alert-001"])
    type: AlertType = Field(examples=["after_hours"])
    room: str = Field(examples=["work2"])
    message: str = Field(examples=["Devices in work2 are on after office hours."])
    triggered_at: datetime = Field(default_factory=datetime.now)
    active: bool = True
