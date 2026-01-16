from dishka import FromDishka
from dishka.integrations.flask import inject
from flask import Blueprint, request, jsonify
from http import HTTPStatus as status

from application.common.dto.device import DeviceDto
from application.operations.command import AddDeviceCommand
from application.operations.query import GetDeviceQuery
from domain.device.value_objects.device_id import DeviceId
from infrastructure.mediatr.mediatr import Sender as Mediator
from presentation.web.param import DeviceBody

DEVICE_CONTROLLER = Blueprint('device', __name__)

@DEVICE_CONTROLLER.post('/')
@inject
def create_device(
        mediator: FromDishka[Mediator],
) -> None:
    body = DeviceBody(**request.get_json())
    command = AddDeviceCommand(
        device_id=DeviceId(body.device_id)
    )
    mediator.send(command)
    return None, status.CREATED.value

@DEVICE_CONTROLLER.get('/')
@inject
def get_list_device(
        mediator: FromDishka[Mediator],
) -> list[DeviceDto | None]:
    query = GetDeviceQuery()
    result = mediator.send(query)
    return jsonify(result), status.OK.value
