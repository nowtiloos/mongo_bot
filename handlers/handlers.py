from pydantic import ValidationError
from services.mongo_service import MongoDBAggregator
from shemas.shemas import SDataIn, SDataOut
from aiogram import Router
from aiogram.types import Message
from database.mongo_db import collection

router = Router()


@router.message()
async def aggregate_handler(message: Message):
    db_aggregator: MongoDBAggregator = MongoDBAggregator(collection_name=collection)
    chat_id = message.from_user.id
    try:
        query: SDataIn = SDataIn.model_validate_json(message.text)
        result: SDataOut = db_aggregator.aggregate_data_by_time(query=query)

        text = str(result.model_dump_json())

        await message.bot.send_message(chat_id, text)

    except ValidationError:
        await message.bot.send_message(chat_id, "Ошибка при разборе JSON-строки или неверные параметры.")
