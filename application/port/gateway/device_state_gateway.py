from abc import ABC, abstractmethod

from application.common.dto.device_state import DeviceStateDto
from domain.device.value_objects.device_id import DeviceId


class DeviceStateGateway(ABC):

    @abstractmethod
    def get_device_state(self, device_id: DeviceId) -> list[DeviceStateDto]:
        """Получение состояния устройства"""
        ...