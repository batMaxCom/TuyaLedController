from domain.device.value_objects.device_id import DeviceId


class Device:
    def __init__(
            self,
            device_id: DeviceId,
            name: str
    ):
        self._device_id = device_id
        self._name = name
