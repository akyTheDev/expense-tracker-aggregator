"""Constants of the project."""

from functools import lru_cache


@lru_cache(maxsize=1)
def get_constants() -> dict[str, str]:
    """Get the constants of the project."""
    return {
        "daily_credit_card_aggregation_table": "daily_credit_card_aggregation",
        "daily_user_aggregation_table": "daily_user_aggregation",
    }
