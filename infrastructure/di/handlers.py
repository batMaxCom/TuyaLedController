from dishka import Provider, Scope, provide_all

from application.operations.command import AddDeviceCommandHandler
from application.operations.query import GetDeviceQueryHandler, GetDevicePropertyQueryHandler, \
    GetDeviceStateQueryHandler


class HandlersProvider(Provider):
    """Провайдер обработчиков."""
    scope = Scope.REQUEST

    command_handlers = provide_all(
        AddDeviceCommandHandler
    )
    query_handlers = provide_all(
        GetDeviceQueryHandler,
        GetDevicePropertyQueryHandler,
        GetDeviceStateQueryHandler
    )
