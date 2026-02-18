from robotic_haircut.models import CutSegment, HeadObservation, SafetyLimits


class SafetyError(RuntimeError):
    pass


class SafetySupervisor:
    """Hard safety checks before and during motion."""

    def __init__(self, limits: SafetyLimits | None = None):
        self.limits = limits or SafetyLimits()
        self._emergency_stop = False

    def trigger_emergency_stop(self) -> None:
        self._emergency_stop = True

    def clear_emergency_stop(self) -> None:
        self._emergency_stop = False

    def validate_observation(self, observation: HeadObservation) -> None:
        if self._emergency_stop:
            raise SafetyError("Emergency stop is active")
        if observation.head_pose_confidence < self.limits.min_pose_confidence:
            raise SafetyError("Pose confidence too low")
        if observation.nearest_obstacle_mm < self.limits.min_obstacle_distance_mm:
            raise SafetyError("Obstacle too close to toolpath")

    def validate_segment(self, segment: CutSegment) -> None:
        if self._emergency_stop:
            raise SafetyError("Emergency stop is active")
        if segment.speed_mm_s > self.limits.max_tool_speed_mm_s:
            raise SafetyError("Segment speed exceeds configured safety limit")
