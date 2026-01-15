from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class DeviceStateDto:
    code: str
    value: Any