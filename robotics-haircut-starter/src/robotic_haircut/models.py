from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class HeadObservation:
    """Simplified observation from vision subsystem."""

    head_pose_confidence: float
    nearest_obstacle_mm: float
    hair_length_zones_mm: List[float]


@dataclass(frozen=True)
class CutSegment:
    """A single path segment the robot should execute."""

    zone_index: int
    target_trim_mm: float
    speed_mm_s: float


@dataclass(frozen=True)
class SafetyLimits:
    min_obstacle_distance_mm: float = 25.0
    max_tool_speed_mm_s: float = 80.0
    min_pose_confidence: float = 0.85
