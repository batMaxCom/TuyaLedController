from flask import Blueprint, request, status, current_app

from application.common.dto.device import DeviceDto
from application.operations.command import AddDeviceCommand
from application.operations.query import GetDeviceQuery
from presentation.web.param import DeviceBody
from presentation.web.schemas.base import SuccessfulResponse

DEVICE_CONTROLLER = Blueprint('device', __name__)
mediator = current_app.extensions["mediator"]

@DEVICE_CONTROLLER.post('/')
def create_device() -> SuccessfulResponse[None]:
    body = DeviceBody(**request.get_json())
    command = AddDeviceCommand(
        device_id=body.device_id
    )
    result = mediator.send(command)
    return SuccessfulResponse(status.HTTP_200_OK, result)

@DEVICE_CONTROLLER.get('/')
def get_list_device(
) -> SuccessfulResponse[list[DeviceDto]]:
    query = GetDeviceQuery()
    result = mediator.send(query)
    return SuccessfulResponse(status.HTTP_200_OK, result)
