from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.bot_db import sql_command_random
from parsers.news import parser




# @dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.chat.id,
                           f'Привет {message.from_user.full_name}, чтобы внести свое блюдо в меню,'
                           f'пропиши команду - \n"/menu"')


#@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Next', callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'Кто перзидент Кыргызстана?'
    otvety = [
        'Садыр Жапаров',
        'Путин',
        'Байдон',
        'Зеленский',
        'Назарбаев'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=otvety,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=20,
        explanation='Лох!',
        reply_markup=markup,
    )


async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await bot.send_message(message.chat.id, "Это должно быть ответом на собщения ")



async def show_random_user(message: types.Message):
    await sql_command_random(message)

async def parser_news(message: types.Message):
    data = parser()
    for item in data:
        await bot.send_message(
            message.from_user.id,
            f'{item["link"]}\n\n'
            f'{item["title"]}\n'
            f'{item["time"]}\n'
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(show_random_user, commands='food')
    dp.register_message_handler(parser_news, commands='news')