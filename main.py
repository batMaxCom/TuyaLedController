from flask import Flask

from application.operations.query import GetDeviceQuery, GetDeviceQueryHandler
from infrastructure.persistence.sqlalchemy.table.device import map_device_table
from presentation.web.controllers.device import DEVICE_CONTROLLER

from application.operations.command import AddDeviceCommand, AddDeviceCommandHandler
from infrastructure.mediatr.mediatr import Mediator
from infrastructure.mediatr.registy import Registry

app = Flask(__name__)

# CQRS
registry = Registry()
registry.add_handler(AddDeviceCommand, AddDeviceCommandHandler)
registry.add_handler(GetDeviceQuery, GetDeviceQueryHandler)

app.extensions["mediator"] = Mediator(registry)

# Controllers
app.register_blueprint(DEVICE_CONTROLLER, url_prefix="/api")

if __name__ == "__main__":
    map_device_table()
    app.run(
        host="0.0.0.0",
        port=8000,
        threaded=True,
        debug=True
    )