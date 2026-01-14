from dishka import make_container
from dishka.integrations.flask import setup_dishka
from flask import Flask

from infrastructure.di.db import DatabaseProvider, SessionProvider
from infrastructure.di.mediator import MediatorProvider
from infrastructure.di.repository.sql_device_repository import RepositoryProvider
from infrastructure.persistence.sqlalchemy.table.device import map_device_table
from presentation.web.controllers.device import DEVICE_CONTROLLER

app = Flask(__name__)

container = make_container(
    DatabaseProvider(),
    SessionProvider(),
    RepositoryProvider(),
    MediatorProvider(),
)

setup_dishka(container, app)


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