from robotic_haircut.models import CutSegment, HeadObservation


class HaircutPlanner:
    """Creates a simple trim plan from observed hair lengths."""

    def __init__(self, desired_length_mm: float = 12.0, default_speed_mm_s: float = 40.0):
        self.desired_length_mm = desired_length_mm
        self.default_speed_mm_s = default_speed_mm_s

    def create_plan(self, observation: HeadObservation) -> list[CutSegment]:
        segments: list[CutSegment] = []
        for idx, zone_len in enumerate(observation.hair_length_zones_mm):
            trim_amount = max(0.0, zone_len - self.desired_length_mm)
            if trim_amount > 0:
                segments.append(
                    CutSegment(
                        zone_index=idx,
                        target_trim_mm=trim_amount,
                        speed_mm_s=self.default_speed_mm_s,
                    )
                )
        return segments
