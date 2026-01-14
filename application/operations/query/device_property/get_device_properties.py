from dataclasses import dataclass

from application.common.handlers import QueryHandler
from application.common.makers import Query
from application.port.gateway.device_property_gateway import DevicePropertyGateway
from domain.device.value_objects.device_id import DeviceId
from domain.device_property.entity import DeviceProperty


@dataclass(frozen=True, slots=True)
class GetDevicePropertyQuery(Query):
    device_id: DeviceId

class GetDevicePropertyHandler(QueryHandler):
    def __init__(
            self,
            device_property_gateway: DevicePropertyGateway,

    ) -> None:
        self.__device_propert_gateway = device_property_gateway

    def handle(self, command: GetDevicePropertyQuery) -> DeviceProperty:
        return self.__device_propert_gateway.get_device_property(command.device_id)
