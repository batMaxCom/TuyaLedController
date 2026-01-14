from dishka import Provider, Scope, provide
from sqlalchemy.orm import Session

from domain.device.repository import DeviceRepository
from infrastructure.mediatr.mediatr import Mediator
from infrastructure.mediatr.registy import Registry
from application.operations.command import (
    AddDeviceCommand,
    AddDeviceCommandHandler,
)
from infrastructure.persistence.sqlalchemy.adapters.repositories.device import SqlDeviceRepositoryImpl

class MediatorProvider(Provider):
    scope = Scope.APP

    @provide
    def registry(self) -> Registry:
        registry = Registry()
        registry.add_handler(
            AddDeviceCommand,
            AddDeviceCommandHandler,
        )
        return registry

    @provide
    def mediator(self, registry: Registry) -> Mediator:
        return Mediator(registry)
