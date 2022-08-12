from aiogram import types
from aiogram.utils import executor
from config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Hello {message.from_user.full_name}')


@dp.message_handler(commands=['game'])
async def game_1(message: types.Message):
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

    @dp.callback_query_handler(lambda call: call.data == 'button_call_1')
    async def game_2(call: types.CallbackQuery):
        markup = InlineKeyboardMarkup()
        button_call_2 = InlineKeyboardButton('Next', callback_data='button_call_2')
        markup.add(button_call_2)

        question = 'Каким инструментом летают ведьмы???'
        otvety = [
            'Истребитель',
            'Чаша',
            'Ковер',
            'Метла',
            'Гр.Авиа Boing 541'
        ]
        await bot.send_poll(
            chat_id=call.message.chat.id,
            question=question,
            options=otvety,
            is_anonymous=False,
            type='quiz',
            correct_option_id=3,
            open_period=20,
            explanation='Полный лох!!!',
            reply_markup=markup,
        )


@dp.message_handler(commands='mem')
async def mem(message: types.Message):
        photo =open('mem/Без названия.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo=photo)




@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.from_user.id , int(message.text ) * int(message.text))
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)