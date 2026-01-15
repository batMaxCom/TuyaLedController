from application.common.dto.device import DeviceDto
from application.port.gateway.device_gateway import DeviceGateway
from domain.device.value_objects.device_id import DeviceId
from infrastructure.tuya_cloud.adapters.device_state_gateway import DeviceStateGatewayImpl
from infrastructure.tuya_cloud.tuya_cloud_manager import tuya_cloud_manager


class DeviceGatewayImpl(DeviceGateway):

    def get_device_info(self, device_id: DeviceId) -> DeviceDto:
        device_info = tuya_cloud_manager.get_device_info(device_id)
        return DeviceDto(
            device_id=device_id,
            name=device_info['result']['name'],
            model=device_info['result']['model'],
            online=device_info['result']['online'],
            status=[
                DeviceStateGatewayImpl._parse_device_status(status)
                for status in device_info['result']['status']
            ]
        )
