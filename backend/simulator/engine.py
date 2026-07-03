import asyncio
import random
from datetime import datetime

from config import settings
from store import alerts, devices, toggle_device
from simulator.alerts import update_alerts


async def random_toggle_step(devices_list: list) -> None:
    count = random.randint(1, 3)
    targets = random.sample(devices_list, min(count, len(devices_list)))
    for device in targets:
        toggle_device(device.id)


async def energy_accumulator_step(devices_list: list, elapsed_seconds: float) -> None:
    elapsed_hours = elapsed_seconds / 3600
    for device in devices_list:
        if device.is_on:
            device.total_energy_kwh_today += device.current_power_w * elapsed_hours / 1000


async def simulation_tick() -> None:
    await random_toggle_step(devices)
    await energy_accumulator_step(devices, settings.simulator_tick_interval)
    update_alerts(devices)


async def run_simulator(broadcast_callback) -> None:
    while True:
        await simulation_tick()
        if broadcast_callback:
            await broadcast_callback()
        await asyncio.sleep(settings.simulator_tick_interval)
