from dataclasses import dataclass

from domain import Device
from domain.device.repository import DeviceRepository


@dataclass(frozen=True, slots=True)
class GetDeviceQuery: ...

class GetDeviceQueryHandler:
    def __init__(
            self,
            repository: DeviceRepository,

    ) -> None:
        self.__repository = repository

    def handle(self) -> list[Device]:
        return self.__repository.get_devices()
