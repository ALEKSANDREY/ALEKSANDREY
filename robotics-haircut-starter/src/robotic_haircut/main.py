import argparse

from robotic_haircut.controller import RobotController
from robotic_haircut.planner import HaircutPlanner
from robotic_haircut.safety import SafetyError, SafetySupervisor
from robotic_haircut.vision import VisionSystem


def run_session(client_name: str, style: str) -> int:
    print(f"Starting haircut simulation for {client_name!r} with style {style!r}")

    vision = VisionSystem()
    planner = HaircutPlanner(desired_length_mm=12.0 if style == "medium-fade" else 16.0)
    safety = SafetySupervisor()
    controller = RobotController(safety=safety)

    try:
        observation = vision.capture_observation()
        safety.validate_observation(observation)
        plan = planner.create_plan(observation)

        if not plan:
            print("No trimming needed.")
            return 0

        for segment in plan:
            result = controller.execute(segment)
            print(result)

        print("Session finished safely (simulation).")
        return 0
    except SafetyError as exc:
        print(f"SAFETY STOP: {exc}")
        return 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Robotic haircut simulator entrypoint")
    parser.add_argument("--client", default="Guest", help="Client display name")
    parser.add_argument("--style", default="medium-fade", help="Target haircut style")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(run_session(client_name=args.client, style=args.style))


if __name__ == "__main__":
    main()
