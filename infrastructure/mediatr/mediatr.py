from infrastructure.mediatr.registy import Registry


class Mediator:
    def __init__(self, registry: Registry) -> None:
        self._registry = registry

    def send(self, request):
        handler_cls = self._registry.get_handler(type(request))
        handler = handler_cls()

        return handler.handle(request)
