from aiogram import types, Dispatcher
from config import bot, ADMIN
import random

# @dp.message_handler()
async def mud(message: types.Message):
    bad_words = ["лох", "петух", "дурак ", "чорт", "жидкий"]
    username = f"@{message.from_user.username}" if message.from_user.username is not None else ""
    if message.text.lower() in bad_words:
        await bot.send_message(
            message.chat.id,
            f"не матерись мал {message.from_user.full_name},"
            f"сам ты {message.text} {username} "
        )
        await bot.delete_message(message.chat.id, message.message_id)
    else:
        pass


def register_handler_extra(dp: Dispatcher):
    dp.register_message_handler(mud)


