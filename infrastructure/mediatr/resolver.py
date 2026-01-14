from typing import cast

from dishka import Container

from application.common.handlers import RequestHandler
from infrastructure.mediatr.interfaces.resolver import Resolver


class DishkaResolver(Resolver):
    """Класс, отвечающий за получения зависимостей."""

    def __init__(self, container: Container) -> None:
        self.__container = container

    def resolve[TDependency: RequestHandler](
        self, dependency_type: type[TDependency]
    ) -> TDependency:
        return cast(TDependency, self.__container.get(dependency_type))
