from sqlalchemy import select
from sqlalchemy.orm import Session

from domain import Device
from domain.device.repository import DeviceRepository


class SqlDeviceRepositoryImpl(DeviceRepository):

    def __init__(self, session: Session) -> None:
        self.__session = session

    model = Device

    def get_devices(self) -> list[Device]:
        stmt = select(Device)
        return list(self.__session.scalars(stmt).all())

    def add_device(self, device: Device) -> None:
        self.__session.add(device)