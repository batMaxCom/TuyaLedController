from dataclasses import dataclass

from application.common.handlers import CommandHandler
from application.common.makers import Command
from domain import Device
from domain.device.repository import DeviceRepository
from domain.device.value_objects.device_id import DeviceId


@dataclass(frozen=True, slots=True)
class AddDeviceCommand(Command):
    device_id: DeviceId

class AddDeviceCommandHandler(CommandHandler):
    def __init__(
            self,
            device_repository: DeviceRepository,

    ) -> None:
        self.__device_repository = device_repository

    def handle(self, command: AddDeviceCommand):
        self.__device_repository.add_device(Device(command.device_id))
