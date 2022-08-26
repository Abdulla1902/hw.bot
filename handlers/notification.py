import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot

# async def get_chat_id(message: types.Message):
#     global chat_id
#     chat_id = message.from_user.id
#     await bot.send_message(chat_id=chat_id, text='Ok!')
#
#
# async def go_to_sleep():
#     await bot.send_message(chat_id=chat_id, text='Time to sleep')
#
# # async def wake_up():
# #     photo = open('mem/mem1.jpg')
# #     await bot.send_photo(chat_id=chat_id, photo=photo,
# #                            caption='waaake!')
#
#
# async def scheduler():
#     aioschedule.every().day.at('15:13').do(go_to_sleep)
#     # aioschedule.every().day.at('15:25').do(wake_up)
#
#
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(2)
#
#
# def register_handler_notification(dp: Dispatcher):
#     dp.register_message_handler(get_chat_id,
#                                 lambda word: 'sleep' in word.text)



async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text='Okeeeey!')


async def time_to_study():
    await bot.send_message(chat_id=chat_id, text='Go study , my brather')


async def scheduler():
    aioschedule.every().friday.at('16:15').do(time_to_study)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(5)

def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'time' in word.text)

