from abc import ABC, abstractmethod
from typing import Any

from application.common.makers import BaseRequest


class RequestHandler[TRequest: BaseRequest[Any], TResponse](ABC):
    @abstractmethod
    def handle(self, request: TRequest) -> TResponse: ...


class CommandHandler[TRequest: BaseRequest[Any], TResponse](
    RequestHandler[TRequest, TResponse]
):
    @abstractmethod
    def handle(self, command: TRequest) -> TResponse: ...


class QueryHandler[TRequest: BaseRequest[Any], TResponse](
    RequestHandler[TRequest, TResponse]
):
    @abstractmethod
    def handle(self, query: TRequest) -> TResponse: ...
