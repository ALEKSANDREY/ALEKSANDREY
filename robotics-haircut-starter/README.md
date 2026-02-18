# Robotic Haircut Starter

A safe-first starter repository for building a **robot-assisted haircut system**.

> ⚠️ This is a development scaffold for simulation and research workflows. Do **not** use on real humans without certified hardware, legal compliance, and safety engineering review.

## What this starter includes

- A modular Python package layout.
- Safety gating layer (hard-stop checks).
- Basic planning + motion simulation loop.
- Camera/vision interface stubs for future integration.
- CLI entrypoint for dry-run simulation.
- Tests for critical safety behaviors.

## Architecture

- `vision.py`: obtains head/hair observations (currently mocked).
- `planner.py`: converts observations into cut segments.
- `safety.py`: enforces safety constraints and emergency stop behavior.
- `controller.py`: executes approved segments in simulation.
- `main.py`: orchestrates full pipeline.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
robotic-haircut --client "Demo User" --style "medium-fade"
pytest
```

## Suggested roadmap

1. Replace mocked observations with your camera/depth pipeline.
2. Integrate a real robot SDK (e.g., ROS2 + arm controller).
3. Add force/torque and proximity sensors.
4. Add real-time re-planning and pause/resume control.
5. Build operator UI with manual override.
6. Add logging/replay for audit and debugging.

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
