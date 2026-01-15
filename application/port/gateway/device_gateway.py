from abc import ABC, abstractmethod

from application.common.dto.device import DeviceDto
from domain.device.value_objects.device_id import DeviceId


class DeviceGateway(ABC):

    @abstractmethod
    def get_device_info(self, device_id: DeviceId) -> DeviceDto:
        """Получение информации о устройстве"""
        ...