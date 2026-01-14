from abc import ABC, abstractmethod

from domain.common.value_objects.property import Property
from domain.device.value_objects.device_id import DeviceId
from domain.device_property.entity import DeviceProperty


class DevicePropertyGateway(ABC):

    @abstractmethod
    def get_device_property(self, device_id: DeviceId) -> DeviceProperty:
        """Получить свойства устройства"""
        ...

    def update_device_property(self, device_id: DeviceId, command: Property): # Response
        """Отправка команды устройству"""
        ...