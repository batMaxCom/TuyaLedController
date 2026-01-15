from dishka import Provider, provide, Scope

from application.port.gateway.device_gateway import DeviceGateway
from application.port.gateway.device_property_gateway import DevicePropertyGateway
from infrastructure.tuya_cloud.adapters.device_gataway import DeviceGatewayImpl
from infrastructure.tuya_cloud.adapters.device_property_gateway import DevicePropertyGatewayImpl


class GatewayProvider(Provider):
    scope = Scope.REQUEST

    device_gateway = provide(DeviceGatewayImpl, provides=DeviceGateway)
    device_property_gateway = provide(DevicePropertyGatewayImpl, provides=DevicePropertyGateway)
