import random
from aiogram import types
from config import bot, ADMIN, Dispatcher


async def game(message: types.Message):
    if message.text.startswith("game") and message.from_user.id in ADMIN:
        lst = ['⚽️', '🏀', '🎰', '🎳' '🎯']
        a = random.choice(lst)
        await bot.send_dice(message.chat.id, emoji=a)
    elif message.text.isdigit():
        await bot.send_message(message.chat.id, int(message.text) * int(message.text))
    elif message.text.lower() == 'dice' and message.from_user.id in ADMIN:
        a = await bot.send_dice(message.chat.id, emoji='🎲')
        await bot.send_message(message.chat.id,
                               'Кости Бота')
        b = await bot.send_dice(message.chat.id, emoji='🎲')
        await bot.send_message(message.chat.id,
                               f'Кости игрока {message.from_user.full_name} @{message.from_user.username}')
        if a.dice.value > b.dice.value:
            await bot.send_message(message.chat.id,
                                   'Победил бот')
        elif a.dice.value == b.dice.value:
            await bot.send_message(message.chat.id, 'Ничья!')
        else:
            await bot.send_message(message.chat.id,
                                   f'Победил игрок {message.from_user.full_name} @{message.from_user.username}')
    else:
        pass




def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(game)

