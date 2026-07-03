from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    simulator_tick_interval: float = 5.0
    alert_after_hours_start: int = 9
    alert_after_hours_end: int = 17
    continuous_on_threshold_hours: float = 2.0

    model_config = {"env_prefix": "OFFICE_"}


settings = Settings()
