"""Test teardown."""

import asyncio
import os
from sys import exit

from tests import get_sql

async def check():
    if os.getenv("DB__HOST") not in ("localhost", "127.0.0.1"):
        print("`DB__HOST` must be localhost for testing.")
        exit(1)


async def teardown():
    sql = get_sql()
    print("Checking test teardown conditions...")
    await check()
    print("Deleting dummy data.")
    with open(
        os.path.join(os.path.dirname(__file__), "teardown.sql"), "r"
    ) as file:
        await sql.execute(file.read())


if __name__ == "__main__":
    asyncio.run(teardown())
    print("Database is cleaning.")
