from sqlalchemy import Column, Table, String

from domain import Device
from infrastructure.persistence.sqlalchemy.table.base import MAPPER_REGISTRY

DEVICE_TABLE = Table(
    "device",
    MAPPER_REGISTRY.metadata,
    Column("id", String, primary_key=True, unique=True)
)

def map_device_table() -> None:
    MAPPER_REGISTRY.map_imperatively(
        Device,
        DEVICE_TABLE,
        properties={
            "_device_id": DEVICE_TABLE.c.id,
        }
    )
