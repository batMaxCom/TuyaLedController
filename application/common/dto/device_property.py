from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Property:
    code: str
    values: dict
    type: str
    name: str
    desc: str


@dataclass(frozen=True, slots=True)
class DevicePropertyDto:
    device_id: str
    properties: list[Property]
