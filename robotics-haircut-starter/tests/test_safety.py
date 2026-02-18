import pytest

from robotic_haircut.models import CutSegment, HeadObservation, SafetyLimits
from robotic_haircut.safety import SafetyError, SafetySupervisor


def test_rejects_low_pose_confidence() -> None:
    safety = SafetySupervisor(SafetyLimits(min_pose_confidence=0.9))
    obs = HeadObservation(
        head_pose_confidence=0.8,
        nearest_obstacle_mm=80,
        hair_length_zones_mm=[20, 20],
    )

    with pytest.raises(SafetyError, match="Pose confidence too low"):
        safety.validate_observation(obs)


def test_rejects_high_speed_segment() -> None:
    safety = SafetySupervisor(SafetyLimits(max_tool_speed_mm_s=50))
    segment = CutSegment(zone_index=1, target_trim_mm=5, speed_mm_s=60)

    with pytest.raises(SafetyError, match="speed exceeds"):
        safety.validate_segment(segment)
