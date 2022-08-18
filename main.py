import logging

from aiogram.utils import executor
from config import dp
from handlers import client, callback, extra, admin, fsm_anketa, fsm_resto

fsm_resto.register_handlers_fsmresto(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
# fsm_anketa.register_handlers_fsmanketa(dp)
admin.register_handlers_admin(dp)
extra.register_handlers_extra(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    logging.basicConfig(level=logging.INFO)