from application.common.dto.device_state import DeviceStateDto
from application.port.gateway.device_state_gateway import DeviceStateGateway
from domain.device.value_objects.device_id import DeviceId
from infrastructure.tuya_cloud.tuya_cloud_manager import tuya_cloud_manager


class DeviceStateGatewayImpl(DeviceStateGateway):

    @staticmethod
    def _parse_device_status(status: dict) -> DeviceStateDto:
        return DeviceStateDto(
            code=status['code'],
            value=status['value']
        )


    def get_device_state(self, device_id: DeviceId) -> list[DeviceStateDto]:
        device_status_list = tuya_cloud_manager.get_device_state(device_id)
        return [
                self._parse_device_status(state)
                for state in device_status_list['result']
            ]
