from dataclasses import dataclass

@dataclass(frozen=True)
class DeviceBody:
    device_id: str