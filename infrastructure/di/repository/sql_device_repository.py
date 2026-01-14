from dishka import Provider, Scope, provide
from sqlalchemy.orm import Session

from domain.device.repository import DeviceRepository
from infrastructure.persistence.sqlalchemy.adapters.repositories.device import SqlDeviceRepositoryImpl


class RepositoryProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def device_repository(
        self,
        session: Session,
    ) -> DeviceRepository:
        return SqlDeviceRepositoryImpl(session)
