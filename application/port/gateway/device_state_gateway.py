from abc import ABC, abstractmethod

from domain.device.value_objects.device_id import DeviceId
from domain.device_state.entity import DeviceState


class DeviceStateGateway(ABC):

    @abstractmethod
    def get_device_state(self, device_id: DeviceId) -> DeviceState:
        """Получение состояния устройства"""
        ...