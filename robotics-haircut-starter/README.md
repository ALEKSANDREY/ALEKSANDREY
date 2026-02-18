# Robotic Haircut Starter

A safe-first starter repository for building a **robot-assisted haircut system**.

> ⚠️ This is a development scaffold for simulation and research workflows. Do **not** use on real humans without certified hardware, legal compliance, and safety engineering review.

## Product vision (your idea)

1. **Phase 1 (Onsite):** people book online and come to your studio/address.
2. **Phase 2 (Mobile):** after successful and safe operations, robot can travel to customer address.

This repo now includes a basic booking policy model that enforces this rollout.

## What this starter includes

- A modular Python package layout.
- Safety gating layer (hard-stop checks).
- Basic planning + motion simulation loop.
- Camera/vision interface stubs for future integration.
- CLI entrypoint for dry-run simulation.
- Booking policy scaffold for onsite-first, mobile-later launch.
- Tests for critical safety behaviors and booking rollout rules.

## Architecture

- `vision.py`: obtains head/hair observations (currently mocked).
- `planner.py`: converts observations into cut segments.
- `safety.py`: enforces safety constraints and emergency stop behavior.
- `controller.py`: executes approved segments in simulation.
- `booking.py`: validates whether mobile bookings are allowed yet.
- `main.py`: orchestrates booking + haircut pipeline.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
robotic-haircut --client "Demo User" --style "medium-fade" --mode onsite --address "Main Studio"
pytest
```

## New rollout commands

Onsite (allowed by default):

```bash
robotic-haircut --client "Alice" --style "medium-fade" --mode onsite --address "123 Market St"
```

Mobile before enablement (blocked intentionally):

```bash
robotic-haircut --client "Alice" --style "medium-fade" --mode mobile --address "555 Pine St"
```

Mobile after enablement flag:

```bash
robotic-haircut --client "Alice" --style "medium-fade" --mode mobile --address "555 Pine St" --mobile-enabled
```

## Suggested roadmap (what to do next)

1. **Booking backend (week 1–2)**
   - Build REST API (`/bookings`, `/availability`, `/cancel`).
   - Add payment + no-show policy.
2. **Operator safety console (week 2–4)**
   - Live video feed, E-stop, “pause/resume”, manual mode.
3. **Perception + control upgrades (month 2)**
   - Replace mock observation with RGB-D/3D head tracking.
   - Add skin-distance estimation and force limits.
4. **Pilot (onsite only, month 3)**
   - Mannequin tests, then supervised human trials.
   - Track incidents, comfort score, haircut quality score.
5. **Mobile pilot (post-success)**
   - Enable `mobile_enabled` in production policy only after KPI thresholds are met.
   - Add travel-time routing + setup checklist at client location.

## Creating your own GitHub repo from this template

1. Create a new empty repo on GitHub, e.g. `robotic-haircut`.
2. Copy this folder contents into that repo root.
3. Run:

```bash
git init
git add .
git commit -m "Initial robotics haircut scaffold"
git branch -M main
git remote add origin git@github.com:<your-user>/robotic-haircut.git
git push -u origin main
```

## Important safety notes

- Add a hardware E-stop independent from software.
- Never run near scalp/skin without validated collision limits.
- Keep a human operator in control at all times.
- Conduct staged testing: simulation → mannequin → supervised trials.
