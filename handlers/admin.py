import random
from aiogram import types
from config import bot, ADMIN, Dispatcher


async def game(message: types.Message):
    if message.from_user.id in ADMIN and message.text.startswith('game'):
        games = ['🏀','🎰','⚽','🎲','🎯','🎳']
        g_games = random.choice(games)
        await bot.send_dice(message.chat.id, emoji=g_games)


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(game)

