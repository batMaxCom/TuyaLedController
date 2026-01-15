from dataclasses import dataclass

@dataclass(frozen=True)
class DeviceBody:
    device_id: str

@dataclass(frozen=True)
class DeviceQuery:
   device_id: str