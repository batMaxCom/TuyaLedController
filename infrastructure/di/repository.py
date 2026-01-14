from dishka import Provider, Scope, provide

from domain.device.repository import DeviceRepository
from infrastructure.persistence.sqlalchemy.adapters.repositories.device import SqlDeviceRepositoryImpl


class RepositoryProvider(Provider):
    scope = Scope.REQUEST

    device_repository = provide(SqlDeviceRepositoryImpl, provides=DeviceRepository)
