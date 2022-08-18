import logging

from aiogram.utils import executor
from config import dp
from handlers import client, callback, extra, admin

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
# admin.register_admin_handlers(dp)
extra.register_handlers_extra(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    logging.basicConfig(level=logging.INFO)