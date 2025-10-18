import asyncio
import sys
from queries.orm import (
    create_tables, 
)

async def main():
    # Create tables
    await create_tables()

if __name__ == "__main__":
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())