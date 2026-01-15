from dataclasses import dataclass

from application.common.dto.device import DeviceDto
from application.port.gateway.device_gateway import DeviceGateway
from domain.device.repository import DeviceRepository
from application.common.handlers import QueryHandler
from application.common.makers import Query


@dataclass(frozen=True, slots=True)
class GetDeviceQuery(Query): ...

class GetDeviceQueryHandler(QueryHandler):
    def __init__(
            self,
            device_repository: DeviceRepository,
            device_gateway: DeviceGateway,

    ) -> None:
        self.__device_repository = device_repository
        self.__device_gateway = device_gateway

    def handle(self, query: GetDeviceQuery) -> list[DeviceDto | None]:
        devices_ids_in_memory = self.__device_repository.get_device_ids()
        device_list_info = [
            self.__device_gateway.get_device_info(device_id)
            for device_id in devices_ids_in_memory
        ] if devices_ids_in_memory else []
        return device_list_info
