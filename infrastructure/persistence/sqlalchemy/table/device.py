from sqlalchemy import Column, Table, Integer, String

from domain import Device
from infrastructure.persistence.sqlalchemy.table.base import MAPPER_REGISTRY

DEVICE_TABLE = Table(
    "device",
    MAPPER_REGISTRY.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False)
)

def map_device_table() -> None:
    MAPPER_REGISTRY.map_imperatively(
        Device,
        DEVICE_TABLE,
        properties={
            "id": DEVICE_TABLE.c.id,
            "name": DEVICE_TABLE.c.name
        }
    )
