from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




# @dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Hello {message.from_user.full_name}')


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



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')