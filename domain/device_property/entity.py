class DeviceProperty:
    def __init__(
            self,
            code: str,
            values: str,
            type: str,
            name: str,
            desc: str

    ):
        self._code = code
        self._values = values
        self._type = type
        self._name = name
        self._desc = desc