from domain.device.value_objects.device_id import DeviceId


class DeviceState:
    def __init__(
            self,
            device_id: DeviceId,
            online: str,
            ip: str,
            last_update: int,
            power: bool


    ):
        self._device_id = device_id
        self._online = online
        self._ip = ip
        self._last_update = last_update
        self._power = power
