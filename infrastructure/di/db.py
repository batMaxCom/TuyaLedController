from dishka import Provider, Scope, provide
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from infrastructure.persistence.sqlalchemy.config import PostgresConfig

class DatabaseProvider(Provider):
    scope = Scope.APP

    @provide
    def engine(self):
        settings = PostgresConfig.from_env()
        return create_engine(settings.uri, pool_pre_ping=True)

    @provide
    def session_factory(self, engine) -> sessionmaker:
        return sessionmaker(
            bind=engine,
            autoflush=False,
            autocommit=False,
        )

class SessionProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def session(self, session_factory) -> Session:
        session = session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
