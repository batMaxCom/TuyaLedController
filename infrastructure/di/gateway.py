from dishka import Provider, provide, Scope

from application.port.gateway.device_gateway import DeviceGateway
from infrastructure.tuya_cloud.adapters.device_gataway import DeviceGatewayImpl


class GatewayProvider(Provider):
    scope = Scope.REQUEST

    device_gateway = provide(DeviceGatewayImpl, provides=DeviceGateway)
