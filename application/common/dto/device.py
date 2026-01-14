from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DeviceDto:
    device_id: str
    name: str
    model: str
    online: bool
    status: dict