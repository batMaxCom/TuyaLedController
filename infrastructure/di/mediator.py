from dishka import Provider, Scope, provide

from application.port.sender import Sender
from infrastructure.di.factories.command_factory import register_commands
from infrastructure.di.factories.query_factory import register_queries
from infrastructure.mediatr.interfaces.resolver import Resolver
from infrastructure.mediatr.mediatr import MediatorImpl
from infrastructure.mediatr.registy import Registry
from infrastructure.mediatr.resolver import DishkaResolver

class MediatorProvider(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.APP)
    def registry(self) -> Registry:
        registry = Registry()
        register_commands(registry)
        register_queries(registry)
        return registry

    mediator = provide(MediatorImpl, provides=Sender)
    resolver = provide(DishkaResolver, provides=Resolver)
