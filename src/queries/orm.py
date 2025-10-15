import logging
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from database import async_engine, session_async
from models import Base
from time_1 import get_utc_now


# -------------------------------
# Настройка логов
logging.basicConfig(
    level=logging.INFO,  # Можно поменять на DEBUG для полной отладки
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

# -------------------------------
async def create_tables():
    logger.info("Создание таблиц в БД...")
    async_engine.echo = False  # Включаем лог SQL
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Таблицы успешно созданы!")

