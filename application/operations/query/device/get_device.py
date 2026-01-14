from dataclasses import dataclass

from domain import Device
from domain.device.repository import DeviceRepository
from application.common.handlers import QueryHandler
from application.common.makers import Query


@dataclass(frozen=True, slots=True)
class GetDeviceQuery(Query): ...

class GetDeviceQueryHandler(QueryHandler):
    def __init__(
            self,
            device_repository: DeviceRepository,

    ) -> None:
        self.__device_repository = device_repository

    def handle(self, query: GetDeviceQuery) -> list[Device]:
        return self.__device_repository.get_devices()
