from dataclasses import asdict

from dishka import FromDishka
from dishka.integrations.flask import inject
from flask import Blueprint
from http import HTTPStatus as status

from application.operations.query import GetDeviceStateQuery
from domain.device.value_objects.device_id import DeviceId
from infrastructure.mediatr.mediatr import Mediator

DEVICE_STATE_CONTROLLER = Blueprint('device_state', __name__)


@DEVICE_STATE_CONTROLLER.get('/<device_id>')
@inject
def get_device_state(
        device_id: str,
        *,
        mediator: FromDishka[Mediator],
) -> dict | None:
    query = GetDeviceStateQuery(DeviceId(device_id))
    result = mediator.send(query)
    return [asdict(state) for state in result], status.OK.value if result else status.NOT_FOUND.value
