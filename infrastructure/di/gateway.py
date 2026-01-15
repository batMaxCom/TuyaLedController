from dishka import Provider, provide, Scope

from application.port.gateway.device_gateway import DeviceGateway
from application.port.gateway.device_property_gateway import DevicePropertyGateway
from application.port.gateway.device_state_gateway import DeviceStateGateway
from infrastructure.tuya_cloud.adapters.device_gataway import DeviceGatewayImpl
from infrastructure.tuya_cloud.adapters.device_property_gateway import DevicePropertyGatewayImpl
from infrastructure.tuya_cloud.adapters.device_state_gateway import DeviceStateGatewayImpl


class GatewayProvider(Provider):
    scope = Scope.REQUEST

    device_gateway = provide(DeviceGatewayImpl, provides=DeviceGateway)
    device_property_gateway = provide(DevicePropertyGatewayImpl, provides=DevicePropertyGateway)
    device_state_gateway = provide(DeviceStateGatewayImpl, provides=DeviceStateGateway)
