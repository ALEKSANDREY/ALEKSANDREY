from robotic_haircut.models import CutSegment
from robotic_haircut.safety import SafetySupervisor


class RobotController:
    """Simulation-only controller.

    Replace with real robot SDK bindings and state feedback.
    """

    def __init__(self, safety: SafetySupervisor):
        self.safety = safety

    def execute(self, segment: CutSegment) -> str:
        self.safety.validate_segment(segment)
        return (
            f"Executed zone={segment.zone_index} trim={segment.target_trim_mm:.1f}mm "
            f"at speed={segment.speed_mm_s:.1f}mm/s"
        )
