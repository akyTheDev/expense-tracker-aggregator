"""Configurations for the project."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class DbSettings(BaseSettings):
    """Db settings for the project.

    Attributes:
        HOST: The hostname of the database.
        PORT: The port number of the database.
        USERNAME: The username of the database.
        PASSWORD: The password of the database.
        NAME: The name of the database.
    """

    model_config = SettingsConfigDict(env_prefix="_")

    HOST: str
    PORT: int
    USERNAME: str
    PASSWORD: str
    NAME: str


class KafkaSettings(BaseSettings):
    """Kafka settings for the project.

    Attributes:
        CLIENT_ID: Client ID of the kafka server.
        BROKER: Broker of the kafka server.
        USERNAME: SASL Username of the kafka server.
        PASSWORD: SASL Password of the kafka server.
        CONSUMER_GROUP: Consumer group of the kafka server.
    """

    CLIENT_ID: str
    BROKER: str
    USERNAME: str
    PASSWORD: str
    CONSUMER_GROUP: str


class Settings(BaseSettings):
    """Settings of the project."""

    model_config = SettingsConfigDict(env_nested_delimiter="__")

    KAFKA: KafkaSettings
    DB: DbSettings
    LOG_LEVEL: str = "info"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Lazily load and cache the settings instance."""
    return Settings()
