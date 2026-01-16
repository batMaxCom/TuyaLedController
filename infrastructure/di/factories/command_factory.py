from application.operations.command import AddDeviceCommand, AddDeviceCommandHandler
from infrastructure.mediatr.registy import Registry


def register_commands(registry: Registry) -> None:
    registry.add_handler(AddDeviceCommand, AddDeviceCommandHandler)