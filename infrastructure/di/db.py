from typing import Generator, Iterable

from dishka import Provider, Scope, provide
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

from infrastructure.persistence.sqlalchemy.config import PostgresConfig

class DatabaseProvider(Provider):
    scope = Scope.APP

    @provide
    def engine(self) -> Engine:
        settings = PostgresConfig.from_env()
        return create_engine(
            settings.uri,
            pool_pre_ping=True,
        )

    @provide
    def session_maker(self, engine: Engine) -> sessionmaker[Session]:
        return sessionmaker(
            bind=engine,
            autoflush=False,
            autocommit=False,
        )

class SessionProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def session(self, session_maker: sessionmaker[Session]) -> Iterable[Session]:
        with session_maker() as session:
            yield session
