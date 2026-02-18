from robotic_haircut.models import HeadObservation


class VisionSystem:
    """Placeholder vision module.

    Replace this with your actual RGB-D / multi-camera inference pipeline.
    """

    def capture_observation(self) -> HeadObservation:
        # Mocked safe observation for local development.
        return HeadObservation(
            head_pose_confidence=0.94,
            nearest_obstacle_mm=40.0,
            hair_length_zones_mm=[22.0, 18.0, 14.0, 16.0],
        )
