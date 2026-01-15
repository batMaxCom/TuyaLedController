from dishka import Provider, provide, Scope

from application.operations.command import AddDeviceCommandHandler
from application.operations.query import GetDeviceQueryHandler
from application.port.gateway.device_gateway import DeviceGateway
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
