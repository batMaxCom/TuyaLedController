from dishka import Provider, Scope, provide

from application.operations.query import GetDeviceQuery, GetDeviceQueryHandler
from application.port.sender import Sender
from infrastructure.mediatr.interfaces.resolver import Resolver
from infrastructure.mediatr.mediatr import Mediator
from infrastructure.mediatr.registy import Registry
from application.operations.command import (
    AddDeviceCommand,
    AddDeviceCommandHandler,
)
from infrastructure.mediatr.resolver import DishkaResolver

class MediatorProvider(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.APP)
    def registry(self) -> Registry:
        registry = Registry()
        registry.add_handler(
            AddDeviceCommand,
            AddDeviceCommandHandler,
        )
        registry.add_handler(
            GetDeviceQuery,
            GetDeviceQueryHandler,
        )
        return registry


    @provide
    def mediator(self, registry: Registry, resolver: Resolver) -> Mediator:
        return Mediator(registry, resolver)

    resolver = provide(DishkaResolver, provides=Resolver)
