from abc import ABC, abstractmethod

from domain.common.value_objects.command import Command
from domain.device.value_objects.device_id import DeviceId
from domain.device_property.entity import DeviceProperty


class DevicePropertyGateway(ABC):

    @abstractmethod
    def get_device_property(self, device_id: DeviceId) -> DeviceProperty:
        """Получить свойства устройства"""
        ...

    def update_device_property(self, device_id: DeviceId, command: Command): # Response
        """Отправка команды устройству"""
        ...