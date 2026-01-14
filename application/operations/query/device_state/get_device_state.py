from dataclasses import dataclass

from application.common.handlers import QueryHandler
from application.common.makers import Query
from application.port.gateway.device_state_gateway import DeviceStateGateway
from domain.device.value_objects.device_id import DeviceId
from domain.device_state.entity import DeviceState


@dataclass(frozen=True, slots=True)
class GetDeviceStateQuery(Query):
    device_id: DeviceId

class GetDeviceStateHandler(QueryHandler):
    def __init__(
            self,
            device_state_gateway: DeviceStateGateway,

    ) -> None:
        self.__device_state_gateway = device_state_gateway

    def handle(self, command: GetDeviceStateQuery) -> DeviceState:
        return self.__device_state_gateway.get_device_state(command.device_id)
