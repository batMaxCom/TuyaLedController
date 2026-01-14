from dishka import FromDishka
from dishka.integrations.flask import inject
from flask import Blueprint, request
from http import HTTPStatus as status

from application.common.dto.device import DeviceDto
from application.operations.command import AddDeviceCommand
from application.operations.query import GetDeviceQuery
from infrastructure.mediatr.mediatr import Mediator
from presentation.web.param import DeviceBody
from presentation.web.schemas.base import SuccessfulResponse

DEVICE_CONTROLLER = Blueprint('device', __name__)

@DEVICE_CONTROLLER.post('/')
@inject
def create_device(
        mediator: FromDishka[Mediator],
) -> SuccessfulResponse[None]:
    body = DeviceBody(**request.get_json())
    command = AddDeviceCommand(
        device_id=body.device_id
    )
    result = mediator.send(command)
    return SuccessfulResponse(status.OK, result)

@DEVICE_CONTROLLER.get('/')
@inject
def get_list_device(
        mediator: FromDishka[Mediator],
) -> SuccessfulResponse[list[DeviceDto]]:
    query = GetDeviceQuery()
    result = mediator.send(query)
    return SuccessfulResponse(status.OK, result)
