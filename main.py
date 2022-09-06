# from aiogram.utils import executor
# from config import dp, bot, URL
# from handlers import client, callback, extra, admin, fsm_resto, notification, inline
# from database import bot_db
# import logging
# import asyncio
# from decouple import config
#
#
# async def on_startup(_):
#     await bot.set_webhook(URL)
#     asyncio.create_task(notification.time_to_study())
#     bot_db.sql_create()
#
#
# async def on_shutdown(dp):
#     await bot.delete_webhook()
#
# inline.register_handler_inline(dp)
# fsm_resto.register_handlers_fsmresto(dp)
# client.register_handlers_client(dp)
# callback.register_handlers_callback(dp)
#
# admin.register_handler_admin(dp)
# notification.register_handler_notification(dp)
#
#
# extra.register_handler_extra(dp)
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     # executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
#     executor.start_webhook(
#         dispatcher=dp,
#         webhook_path="",
#         on_startup=on_startup,
#         on_shutdown=on_shutdown,
#         skip_updates=True,
#         host='0.0.0.0',
#         port=config("PORT", default=5000)
#     )



import logging


from aiogram.utils import executor
from config import dp, bot
from handlers import client, callback, extra, admin, fsm_resto, notification, inline
from database import bot_db
import asyncio
from decouple import config


async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    bot_db.sql_create()

async def on_shutdown(dp):
    await bot.delete_webhook()


inline.register_handler_inline(dp)
notification.register_handler_notification(dp)
fsm_resto.register_handlers_fsmresto(dp)
# fsm_anketa.register_handlers_fsmanketa(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handler_admin(dp)
extra.register_handler_extra(dp)






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    logging.basicConfig(level=logging.INFO)


