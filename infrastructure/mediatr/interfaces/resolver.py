from abc import ABC, abstractmethod

from application.common.handlers import RequestHandler


class Resolver(ABC):
    @abstractmethod
    def resolve[TDependency: RequestHandler](
        self, dependency_type: type[TDependency]
    ) -> TDependency: ...
