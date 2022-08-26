from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import dp, bot



#@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
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



#@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_3(call: types.CallbackQuery):


        question = 'Как зовут гг персонажа в аниме Наруто'
        otvety = [
            'Сакура',
            'Какаши',
            'Наруто',
            'Саске',
            'Абдулла'
        ]
        await bot.send_poll(
            chat_id=call.message.chat.id,
            question=question,
            options=otvety,
            is_anonymous=False,
            type='quiz',
            correct_option_id=2,
            open_period=20,
            explanation='Полный лох!!!',
        )






@dp.message_handler(commands='mem')
async def mem(message: types.Message):
        photo = open('mem/mem1.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo=photo)


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")
    # dp.register_message_handler(mem, lambda call: start_handler, commands='mem')

