from dataclasses import dataclass
from os import environ
from typing import Self


@dataclass(frozen=True)
class TuyaCloudConfig:
    """Класс конфигурации для TuyaCloud."""

    access_id: str
    access_key: str
    api_endpoint: str

    @classmethod
    def from_env(cls) -> Self:
        """Возвращает настройки TuyaCloud."""
        access_id = environ.get("ACCESS_ID", "")
        access_key = environ.get("ACCESS_KEY", "")
        api_endpoint = environ.get("API_ENDPOINT", "")


        return cls(
            access_id=access_id,
            access_key=access_key,
            api_endpoint=api_endpoint,
        )