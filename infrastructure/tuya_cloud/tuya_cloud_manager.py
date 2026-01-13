import json
import os
from datetime import datetime

from tuya_connector import TuyaOpenAPI

from infrastructure.tuya_cloud.config import TuyaCloudConfig
from infrastructure.tuya_cloud.enum import TuyaCloudUriEnum


class TuyaCloudManager:
    def __init__(self, access_id, access_key, device_id, endpoint):
        self.device_id = device_id
        self.openapi = TuyaOpenAPI(endpoint, access_id, access_key)
        self.openapi.connect()

    @staticmethod
    def _parse_device_status(api_response: dict) -> dict:
        """
        Преобразует ответ Tuya API в удобный словарь состояния устройства
        """
        result = api_response.get("result", {})
        status_list = result.get("status", [])

        parsed = {
            "device_name": result.get("name"),
            "online": result.get("online"),
            "ip": result.get("ip"),
            "last_update": datetime.fromtimestamp(result.get("update_time", 0)),
            "power": None,
            "mode": None,
            "color": None,
            "countdown": None
        }

        for item in status_list:
            code = item.get("code")
            value = item.get("value")

            if code == "switch_led":
                parsed["power"] = "ON" if value else "OFF"

            elif code == "work_mode":
                parsed["mode"] = value

            elif code == "colour_data":
                if isinstance(value, str):
                    value = json.loads(value)
                parsed["color"] = {
                    "h": value.get("h"),
                    "s": value.get("s"),
                    "v": value.get("v")
                }

            elif code == "countdown":
                parsed["countdown"] = value

        return parsed

    def send_command(self, commands):
        return self.openapi.post(
            f"/v1.0/devices/{self.device_id}/commands",
            {"commands": commands}
        )


    def get_status(self):
        return self._parse_device_status(
            self.openapi.get(TuyaCloudUriEnum.get_info.value.format(self.device_id))
        )
tuya_settings = TuyaCloudConfig.from_env()
controller = TuyaCloudManager(
    access_id=tuya_settings.access_id,
    access_key=tuya_settings.access_key,
    device_id=os.getenv("DEVICE_ID"),
    endpoint=tuya_settings.api_endpoint
)
