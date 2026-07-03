import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router
from api.ws import manager
from simulator.engine import run_simulator
from store import initialize_devices

simulator_task: asyncio.Task | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_devices()
    global simulator_task
    simulator_task = asyncio.create_task(run_simulator(manager.broadcast_state))
    yield
    if simulator_task:
        simulator_task.cancel()
        try:
            await simulator_task
        except asyncio.CancelledError:
            pass


app = FastAPI(title="Office Device Monitor", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    return {"status": "ok", "devices": 15}


@app.websocket("/ws/devices")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    await manager.broadcast_state()
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
