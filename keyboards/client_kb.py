from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_button = KeyboardButton('Cancel')
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(cancel_button)


gender_girl = KeyboardButton('Девушка')
gender_boy = KeyboardButton('Парень')
gender_u = KeyboardButton('Я не знаю')
gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True).add(gender_boy, gender_girl, gender_u)

kg_but = KeyboardButton('Kyrgyzstan')
ru_but = KeyboardButton('Russia')
us_but = KeyboardButton('USA')
ch_but = KeyboardButton('China')
resto_nat = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True).row(kg_but, ru_but, us_but, ch_but)