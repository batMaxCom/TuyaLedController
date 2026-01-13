from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from infrastructure.persistence.sqlalchemy.config import PostgresConfig

settings = PostgresConfig.from_env()
engine = create_engine(settings.uri)
session = sessionmaker(engine)
