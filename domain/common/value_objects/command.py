from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class Command:

    property: str
    value: Any