from dataclasses import dataclass
from typing import Any

from application.port.gateway.device_property_gateway import DevicePropertyGateway
from domain import Device
from domain.common.value_objects.command import Command
from domain.device.repository import DeviceRepository
from domain.device.value_objects.device_id import DeviceId


@dataclass(frozen=True, slots=True)
class UpdateDevicePropertyCommand:
    device_id: DeviceId
    property: str
    value: Any


class UpdateDevicePropertyCommandHandler:
    def __init__(
            self,
            device_property_gateway: DevicePropertyGateway,

    ) -> None:
        self.__device_property_gateway = device_property_gateway

    def handle(self, command: UpdateDevicePropertyCommand): # Response
        return self.__device_property_gateway.update_device_property(
            Device(
                command.device_id,
                Command(command.property, command.value)
            )
        )
