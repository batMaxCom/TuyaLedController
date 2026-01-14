from dishka import Provider, provide, Scope

from application.operations.command import AddDeviceCommandHandler
from application.operations.query import GetDeviceQueryHandler
from domain.device.repository import DeviceRepository


class HandlersProvider(Provider):
    """Провайдер обработчиков."""
    scope = Scope.REQUEST

    @provide
    def get_device_query_handler(
            self,
            device_repository: DeviceRepository,
    ) -> GetDeviceQueryHandler:
        return GetDeviceQueryHandler(
            device_repository=device_repository,
        )
