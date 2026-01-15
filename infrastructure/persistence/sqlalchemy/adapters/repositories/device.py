from sqlalchemy import select
from sqlalchemy.orm import Session

from domain import Device
from domain.device.repository import DeviceRepository
from domain.device.value_objects.device_id import DeviceId
from infrastructure.persistence.sqlalchemy.table.device import DEVICE_TABLE


class SqlDeviceRepositoryImpl(DeviceRepository):

    def __init__(self, session: Session) -> None:
        self.__session = session

    model = Device

    def get_device_ids(self) -> list[DeviceId]:
        stmt = select(DEVICE_TABLE.c.id)
        return [DeviceId(v) for v in self.__session.scalars(stmt)]

    def add_device(self, device: Device) -> None:
        self.__session.add(device)
        self.__session.commit()