import json

from application.common.dto.device_property import DevicePropertyDto, Property
from application.port.gateway.device_property_gateway import DevicePropertyGateway
from domain.device.value_objects.device_id import DeviceId
from infrastructure.tuya_cloud.tuya_cloud_manager import tuya_cloud_manager


class DevicePropertyGatewayImpl(DevicePropertyGateway):

    @staticmethod
    def _parse_device_property(device_property:dict) -> Property:
        return Property(
            code=device_property["code"],
            values=json.loads(device_property["values"]),
            type=device_property["type"],
            name=device_property["name"],
            desc=device_property["desc"]
        )


    def get_device_property(self, device_id: DeviceId) -> DevicePropertyDto:
        device_property = tuya_cloud_manager.get_device_property(device_id)
        return DevicePropertyDto(
            device_id=device_id,
            properties=[
                self._parse_device_property(property)
                for property in device_property['result']['functions']
            ]
        )
