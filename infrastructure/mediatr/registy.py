class Registry:
    def __init__(self) -> None:
        self._handlers: dict[type, type] = {}

    def add_handler(self, request_type: type, handler_type: type) -> None:
        self._handlers[request_type] = handler_type

    def get_handler(self, request_type: type) -> type:
        try:
            return self._handlers[request_type]
        except KeyError:
            raise ValueError(
                f"No handler registered for {request_type.__name__}"
            )