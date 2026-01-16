from application.operations.query import GetDeviceQuery, GetDevicePropertyQuery, GetDeviceStateQuery, \
    GetDeviceStateQueryHandler, GetDevicePropertyQueryHandler, GetDeviceQueryHandler
from infrastructure.mediatr.registy import Registry


def register_queries(registry: Registry) -> None:
    registry.add_handler(GetDeviceQuery, GetDeviceQueryHandler)
    registry.add_handler(GetDevicePropertyQuery, GetDevicePropertyQueryHandler)
    registry.add_handler(GetDeviceStateQuery, GetDeviceStateQueryHandler)

