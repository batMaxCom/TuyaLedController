from enum import Enum


class TuyaCloudUriEnum(Enum):

    get_property = "/v1.0/devices/{device_id}/commands"
    get_info = "/v1.0/devices/{device_id}"
