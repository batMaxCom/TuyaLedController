from domain.device.value_objects.device_id import DeviceId


class Device:
    def __init__(
            self,
            device_id: DeviceId,
    ):
        self._device_id = device_id

    @property
    def device_id(self) -> DeviceId:
        return self._device_id