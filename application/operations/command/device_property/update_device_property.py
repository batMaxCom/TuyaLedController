from dataclasses import dataclass
from typing import Any

from application.common.handlers import CommandHandler
from application.port.gateway.device_property_gateway import DevicePropertyGateway
from domain import Device
from domain.common.value_objects.property import Property
from domain.device.value_objects.device_id import DeviceId


@dataclass(frozen=True, slots=True)
class UpdateDevicePropertyCommand(Property):
    device_id: DeviceId
    property: str
    value: Any


class UpdateDevicePropertyCommandHandler(CommandHandler):
    def __init__(
            self,
            device_property_gateway: DevicePropertyGateway,

    ) -> None:
        self.__device_property_gateway = device_property_gateway

    def handle(self, command: UpdateDevicePropertyCommand): # Response
        return self.__device_property_gateway.update_device_property(
            Device(
                command.device_id,
                Property(command.property, command.value)
            )
        )
