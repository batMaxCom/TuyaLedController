from abc import ABC, abstractmethod

from application.common.makers import BaseRequest


class Sender(ABC):
    @abstractmethod
    def send[TResponse](self, request: BaseRequest[TResponse]) -> TResponse: ...
