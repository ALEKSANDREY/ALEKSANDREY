from datetime import datetime

import pytest

from robotic_haircut.booking import BookingPolicy, BookingRequest, ServiceMode


def test_mobile_booking_blocked_when_disabled() -> None:
    policy = BookingPolicy(mobile_enabled=False)
    req = BookingRequest(
        client_name="Andre",
        start_at=datetime.utcnow(),
        style="medium-fade",
        mode=ServiceMode.MOBILE,
        address="555 Pine St",
    )

    with pytest.raises(ValueError, match="not enabled"):
        policy.validate(req)


def test_mobile_booking_allowed_when_enabled() -> None:
    policy = BookingPolicy(mobile_enabled=True)
    req = BookingRequest(
        client_name="Andre",
        start_at=datetime.utcnow(),
        style="medium-fade",
        mode=ServiceMode.MOBILE,
        address="555 Pine St",
    )

    policy.validate(req)
