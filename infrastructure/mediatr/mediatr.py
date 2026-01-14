from application.port.sender import Sender
from infrastructure.mediatr.interfaces.resolver import Resolver
from infrastructure.mediatr.registy import Registry


class Mediator(Sender):
    def __init__(self, registry: Registry, resolver: Resolver) -> None:
        self.__registry = registry
        self.__resolver = resolver

    def send(self, request):
        handler_cls = self.__registry.get_handler(type(request))
        request_handler = self.__resolver.resolve(handler_cls)
        return request_handler.handle(request)
