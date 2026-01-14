from dataclasses import dataclass

from domain import Device
from domain.device.repository import DeviceRepository
from domain.device.value_objects.device_id import DeviceId


@dataclass(frozen=True, slots=True)
class AddDeviceCommand:
    device_id: DeviceId

class AddDeviceCommandHandler:
    def __init__(
            self,
            repository: DeviceRepository,

    ) -> None:
        self.__repository = repository

    def handle(self, command: AddDeviceCommand):
        self.__repository.add_device(Device(command.device_id))
