# Lights, Fans, Discord — System Architecture

## 1. Overview

A single backend acts as the source of truth for 18 simulated devices (3 rooms × 2 fans × 3 lights). Two client interfaces — a real-time web dashboard and a Discord bot — read from and (optionally) act on that same backend, so both always reflect identical state.

```
[Device Simulator] → [Backend API + Store] → [WebSocket] → [Web Dashboard]
                                            → [REST API]  → [Discord Bot]
```

---

## 2. Components

### 2.1 Device Simulator
- Runs as a background task inside the backend (e.g., `asyncio` loop).
- Periodically (every N seconds) randomly toggles a subset of devices on/off.
- Also exposes a **manual override** path (an internal function or endpoint) so devices can be forced on/off — needed for reliably demoing alert conditions in the video.
- On every state change:
  - Updates `status`
  - Updates `last_changed` timestamp
  - Recalculates `current_power`

### 2.2 Energy Accumulator
- A separate periodic tick (e.g., every few seconds) that, for every device currently `ON`, adds `current_power × elapsed_time` to that device's (and the room's, and the office's) running energy total.
- Powers the `kWh`-style "today's usage" figures — distinct from instantaneous wattage.
- Resets daily (or on demo restart).

### 2.3 Backend API (single source of truth)
- **Owns** the in-memory (or lightweight DB-backed) device store — 18 device records.
- Exposes:
  - `GET /devices` — full state of all 18 devices
  - `GET /rooms/{room}` — state for one room
  - `GET /usage` — current total wattage + accumulated kWh (office-wide and per-room)
  - `GET /alerts` — active anomaly conditions
  - `WS /ws/devices` — push channel for live updates (used by dashboard)
- Both the dashboard and the bot query this API; neither holds its own copy of the truth.

### 2.4 Web Dashboard
- Subscribes to the WebSocket (or polls REST on an interval) — no manual refresh needed.
- **Live Device Status Panel** — all 18 devices, grouped by room, with on/off indicators.
- **Live Power Meter** — total office wattage + per-room breakdown, updates alongside device panel.
- **Active Alerts Panel** — timestamped anomalies (see §3).
- *(Bonus)* Top-view office layout with lights glowing / fans animating based on live state.

### 2.5 Discord Bot
- Stateless with respect to device data — on every command, calls the backend REST API fresh.
- Commands:
  | Command | Behavior |
  |---|---|
  | `!status` | Summarized on/off state per room |
  | `!room <name>` | State of one specific room |
  | `!usage` | Current total wattage + today's estimated kWh |
- Responses are passed through an LLM call to phrase results conversationally rather than as raw data dumps.
- *(Bonus)* Proactively posts to a designated channel when an alert condition triggers (bot polls `/alerts` or subscribes to backend alert events).

### 2.6 Hardware/Electrical Schematic (Wokwi)
- Concept-only circuit for **one representative room**.
- ESP32 (or Arduino) reading device on/off state, optionally with a current-sensing component (e.g., ACS712) to demonstrate how real wattage sensing would work.
- Relays used to represent switching fans/lights.
- Not wired for all 18 devices — one room is sufficient to demonstrate the wiring pattern.

---

## 3. Alert Logic

| Condition | Trigger |
|---|---|
| After-hours device on | Any device `status = ON` outside 9 AM–5 PM |
| Room left running | All devices in a room have been continuously `ON` for > 2 hours |

Alerts are timestamped and surfaced both on the dashboard (Active Alerts Panel) and, for the bonus, pushed proactively to Discord.

---

## 4. Data Model (per device)

```
{
  id: string,
  type: "fan" | "light",
  room: "drawing" | "work1" | "work2",
  status: "on" | "off",
  wattage: number,          // rated draw when on (fan: 60W, light: 15W)
  current_power: number,    // 0 if off, wattage if on
  energy_today_kwh: number, // accumulated, resets daily
  last_changed: timestamp
}
```

---

## 5. Why This Architecture

- **Single backend / shared state**: satisfies the hard architecture requirement — dashboard and bot can never disagree, since neither owns its own data.
- **Simulator decoupled from API**: lets the "device layer" evolve (later swapped for real hardware) without touching how dashboard/bot consume data.
- **WebSocket for dashboard, REST for bot**: matches each client's actual need — dashboard needs push/real-time, bot only needs on-demand fresh reads.
- **Separate instantaneous power vs. accumulated energy**: required to correctly support both the live wattage meter and the "kWh today" figure — conflating them would make the accumulated usage stat meaningless.

---

## 6. Bonus Points Opportunities

- **Visual office layout on dashboard** — top-view floor plan (as given in the spec) with lights glowing when ON and fans animating when running, instead of a plain list/table view.
- **Proactive Discord alerts** — bot automatically posts to a designated channel when an alert condition fires (e.g., "Work Room 2 still has 2 fans and 3 lights ON and it's 10 PM"), rather than only responding to commands.
- **LLM-generated conversational responses** — using an LLM to phrase bot replies (and optionally alert messages) in a friendly, humanized tone rather than raw data dumps — explicitly encouraged in the evaluation criteria.
