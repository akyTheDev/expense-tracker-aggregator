"""Logger functions for all modules."""

import logging
from functools import lru_cache

from .config import get_settings

logging.basicConfig(
    level=logging.DEBUG,
    format=("%(asctime)s::%(levelname)s::%(message)s"),
    datefmt="%y-%m-%d-%H:%M:%S",
    handlers=[logging.StreamHandler()],
)


@lru_cache(maxsize=1)
def get_logger() -> logging.Logger:
    """Return logger object."""
    return logging.getLogger()


get_logger().setLevel(get_settings().LOG_LEVEL.upper())
