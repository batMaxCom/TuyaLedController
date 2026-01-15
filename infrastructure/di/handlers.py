from dishka import Provider, provide, Scope

from application.operations.command import AddDeviceCommandHandler
from application.operations.query import GetDeviceQueryHandler, GetDevicePropertyQueryHandler, \
    GetDeviceStateQueryHandler
from application.port.gateway.device_gateway import DeviceGateway
from application.port.gateway.device_property_gateway import DevicePropertyGateway
from application.port.gateway.device_state_gateway import DeviceStateGateway
from domain.device.repository import DeviceRepository


class HandlersProvider(Provider):
    """Провайдер обработчиков."""
    scope = Scope.REQUEST

    @provide
    def get_device_query_handler(
            self,
            device_repository: DeviceRepository,
            device_gateway: DeviceGateway,
    ) -> GetDeviceQueryHandler:
        return GetDeviceQueryHandler(
            device_repository=device_repository,
            device_gateway=device_gateway
        )

    @provide
    def add_device_command_handler(
            self,
            device_repository: DeviceRepository,
    ) -> AddDeviceCommandHandler:
        return AddDeviceCommandHandler(
            device_repository=device_repository
        )

    @provide
    def get_device_property_query_handler(
            self,
            device_property_gateway: DevicePropertyGateway,
    ) -> GetDevicePropertyQueryHandler:
        return GetDevicePropertyQueryHandler(
            device_property_gateway=device_property_gateway
        )

    @provide
    def get_device_state_query_handler(
            self,
            device_state_gateway: DeviceStateGateway,
    ) -> GetDeviceStateQueryHandler:
        return GetDeviceStateQueryHandler(
            device_state_gateway=device_state_gateway
        )
