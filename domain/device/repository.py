from abc import ABC, abstractmethod

from domain import Device
from domain.device.value_objects.device_id import DeviceId


class DeviceRepository(ABC):
    @abstractmethod
    def get_device_ids(self) -> list[DeviceId]: ...

    @abstractmethod
    def add_device(self, device: Device) -> None: ...
