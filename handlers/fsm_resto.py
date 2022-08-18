from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMIN, bot
from keyboards.client_kb import cancel_markup, resto_nat


class FSMResto(StatesGroup):
    photo = State()
    name = State()
    description = State()
    nation = State()
    price = State()

async def fsm_resto_start(message: types.Message):
    if message.from_user.id in ADMIN:
        await FSMResto.photo.set()
        await message.answer('Пожалуйста, отправьте фото блюды!',
                             reply_markup=cancel_markup)
    else:
        await message.reply(f'Доступ разрещен только для Администратора @{message.from_user.username}')


async def fsm_resto_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMResto.next()
    await message.answer('Как называется вашe блюдо?')


async def fsm_resto_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMResto.next()
    await message.answer('Опишите свое блюдо...')



async def fsm_resto_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMResto.next()
    await message.answer('Национальная блюдо какой страны?',
                          reply_markup=resto_nat)


async def fsm_resto_nation(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['nation'] = message.text
    await FSMResto.next()
    await message.answer('Сколько стоит ваша еда?')


async def fsm_resto_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
        await bot.send_photo(message.from_user.id, data['photo'],
                             caption=f'Name: {data["name"]}\n'
                                     f'Description: {data["description"]}\n'
                                     f'Nation: {data["nation"]}\n'
                                     f'Price: {data["price"]}\n')
    await state.finish()
    await message.answer('Внесение окончено!')


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer('Внесение отменено!')


def register_handlers_fsmresto(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state='*', commands='cancel')
    dp.register_message_handler(cancel_registration,
                                Text(equals='cancel'.lower(), ignore_case=True),state='*' )
    dp.register_message_handler(fsm_resto_start, commands=['menu'])
    dp.register_message_handler(fsm_resto_photo, state=FSMResto.photo,
                                content_types=['photo'])
    dp.register_message_handler(fsm_resto_name, state=FSMResto.name)
    dp.register_message_handler(fsm_resto_description, state=FSMResto.description)
    dp.register_message_handler(fsm_resto_nation, state=FSMResto.nation)
    dp.register_message_handler(fsm_resto_price, state=FSMResto.price)

