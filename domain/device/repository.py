from abc import ABC, abstractmethod

from domain import Device


class DeviceRepository(ABC):
    @abstractmethod
    def get_devices(self) -> list[Device]: ...

    @abstractmethod
    def add_device(self, device: Device) -> None: ...
