from dataclasses import asdict

from dishka import FromDishka
from dishka.integrations.flask import inject
from flask import Blueprint
from http import HTTPStatus as status

from application.operations.query import  GetDevicePropertyQuery
from domain.device.value_objects.device_id import DeviceId
from infrastructure.mediatr.mediatr import Mediator

DEVICE_PROPERTY_CONTROLLER = Blueprint('device_property', __name__)


@DEVICE_PROPERTY_CONTROLLER.get('/<device_id>')
@inject
def get_list_device(
        device_id: str,
        *,
        mediator: FromDishka[Mediator],
) -> dict | None:
    query = GetDevicePropertyQuery(DeviceId(device_id))
    result = mediator.send(query)
    return asdict(result), status.OK.value if result else status.NOT_FOUND.value
