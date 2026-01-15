from dataclasses import dataclass

from application.common.dto.device_state import DeviceStateDto


@dataclass(frozen=True, slots=True)
class DeviceDto:
    device_id: str
    name: str
    model: str
    online: bool
    status: list[DeviceStateDto]
