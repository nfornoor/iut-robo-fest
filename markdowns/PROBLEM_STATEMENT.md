# Problem Statement — "Lights, Fans, Discord: The Boss's Big Idea"

**Event:** Techathon Nationals & Rover Summit — Preliminary Round
**Organizers:** IUT Robotics Society / Okkhor Technology

---

## 1. Scenario

An office runs entirely on Discord for communication, but people keep leaving lights and fans on when they go home, driving up the electricity bill. The boss wants a system to monitor every electrical device in the office — live — through both a web dashboard and a Discord bot.

## 2. Fixed Office Setup

- **3 rooms:** Drawing Room (waiting area), Work Room 1 (employees), Work Room 2 (employees)
- **Every room has:** 2 fans + 3 lights = 6 devices/room
- **Total:** 18 devices (6 fans, 9 lights) across the office

## 3. Required Deliverables

| # | Deliverable | Details |
|---|---|---|
| 1 | **System diagram** | Full data flow: devices → simulated data → backend → web dashboard + Discord bot → user. Mermaid is **not allowed**; any other tool or hand-drawn is fine. |
| 2 | **Hardware/circuit schematic** | Built in Wokwi or Tinkercad. Shows how a microcontroller (ESP32/Arduino) would read device on/off state (and optionally current draw) in real life. Only **one representative room** needs to be wired, not all 18 devices. Concept-only, no physical hardware required. |
| 3 | **Simulated device data** | Since there's no real hardware, generate dummy data for all 18 devices with: status (on/off), power draw (W), room, and last-changed timestamp. Data must be **dynamic** — changing over time, not static. |
| 4 | **Web dashboard** | Real-time, no manual refresh. Must include: <br>• **Live device status panel** — all 18 devices, grouped by room, with visual on/off indicators<br>• **Live power meter** — total wattage + per-room breakdown, updating live<br>• **Active alerts panel** — timestamped anomalies (device on after office hours 9AM–5PM; a room with all devices continuously on for >2 hrs)<br>*(Bonus: animated top-view office layout with glowing lights / spinning fans)* |
| 5 | **Discord bot** | Answers on demand, pulling from the **same backend** as the dashboard. Minimum commands:<br>• `!status` — full office summary<br>• `!room <name>` — one room's status<br>• `!usage` — current watts + estimated kWh today<br>Responses must be built from real simulated data (not hardcoded/random), and should sound friendly/humanized — using an LLM to phrase replies is encouraged.<br>*(Bonus: bot proactively posts to a channel when an alert triggers)* |

## 4. Architecture Requirement

One backend is the single source of truth. Both the web dashboard and the Discord bot read from it — neither has its own separate copy of device state.

```
[Simulated Device Layer] → [Backend API] → [Web UI] && [Discord Bot]
```

## 5. Clarifications Given

1. No physical hardware needed — everything is simulated.
2. Dashboard and bot must always reflect the same live data.
3. Dashboard must update without a manual page refresh.
4. Exact command names, UI layout, and visual design are up to the team.
5. Any language, library, or AI/LLM is allowed.
6. Explore both Wokwi and Tinkercad before choosing — one may suit AI-assisted development better.

## 6. Evaluation Criteria

| Criterion | Weight |
|---|---|
| Working web dashboard with real-time data | 20% |
| Clear, correct system diagram | 15% |
| Sensible circuit schematic | 15% |
| Quality of demo & dummy data simulation | 15% |
| Well-structured, documented codebase & commits | 15% |
| Working Discord bot reflecting real simulated data | 10% |
| Dashboard visuals and UX quality | 10% |

## 7. Final Deliverables

- **Public codebase** (e.g., GitHub repo) with a clear README covering setup/run instructions for backend, dashboard, and bot, plus all diagrams included in the repo.
- **Video demo**, max 3 minutes preferred, showing the live dashboard, the Discord bot in action, and briefly explaining the data flow/architecture.

---

## Summary (TL;DR)

Build a fake "smart office" monitoring system: 18 devices (fans + lights) across 3 rooms with simulated, constantly-changing on/off states and power draw. One backend holds this data as the single source of truth. A live web dashboard shows device status, real-time power usage, and alerts (left on after hours, or on too long) without needing a refresh. A Discord bot answers status/usage questions from the same backend, ideally with friendly LLM-phrased replies. You also need to document the design with a system diagram and a one-room circuit schematic (Wokwi/Tinkercad) showing how this would work with real hardware — even though no physical hardware is required. Everything gets submitted as a public repo with a README, plus a short demo video.

---

## Note on the Source PDF

The uploaded document's final paragraph contains text formatted as instructions to an AI assistant (directives about asking clarifying questions, wiring tables, and a specific "dummy dataset" of names/emails/phone numbers). That content doesn't fit the actual assignment — this project needs *device* data, not personal contact records — so it appears to be injected/unrelated text rather than part of the real problem statement, and has been excluded from this summary.
