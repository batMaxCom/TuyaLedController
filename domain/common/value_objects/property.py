from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class Property:

    property: str
    value: Any