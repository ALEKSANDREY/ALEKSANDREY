from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class ServiceMode(str, Enum):
    ONSITE = "onsite"
    MOBILE = "mobile"


@dataclass(frozen=True)
class BookingRequest:
    client_name: str
    start_at: datetime
    style: str
    mode: ServiceMode
    address: str


@dataclass(frozen=True)
class BookingPolicy:
    """Simple launch policy.

    Start in onsite mode only. Enable mobile after operations/safety proof.
    """

    mobile_enabled: bool = False

    def validate(self, request: BookingRequest) -> None:
        if request.mode is ServiceMode.MOBILE and not self.mobile_enabled:
            raise ValueError(
                "Mobile appointments are not enabled yet. "
                "Please book onsite service first."
            )
