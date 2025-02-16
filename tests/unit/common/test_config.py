"""Unit tests for config."""

from src.common import get_settings


class TestGetSettings:

    def test_settings(self):
        """Test settings object."""
        settings = get_settings()

        assert settings.DB.NAME == "postgres"
        assert settings.DB.HOST == "localhost"
        assert settings.DB.USERNAME == "username"
        assert settings.DB.PASSWORD == "password"
        assert settings.DB.PORT == 5433
        assert settings.LOG_LEVEL == "info"
        assert settings.KAFKA.BROKER == "localhost:59092"
        assert settings.KAFKA.CLIENT_ID == "kafka-client"
        assert settings.KAFKA.USERNAME == "admin"
        assert settings.KAFKA.PASSWORD == "password"
        assert settings.KAFKA.CONSUMER_GROUP == "expense-tracker-aggregator"

