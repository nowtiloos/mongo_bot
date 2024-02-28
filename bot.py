import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import settings

from handlers.handlers import router

bot: Bot = Bot(token=settings.BOT_TOKEN)
dp: Dispatcher = Dispatcher()

logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
               "[%(asctime)s] - %(name)s - %(message)s",
    )

    logger.info("Starting bot")

    dp.include_router(router=router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
