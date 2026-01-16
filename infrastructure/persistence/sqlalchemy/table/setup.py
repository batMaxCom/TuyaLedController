from infrastructure.persistence.sqlalchemy.table.device import map_device_table


def setup_mappings() -> None:
    """Сборка маппингов для таблиц БД."""
    map_device_table()