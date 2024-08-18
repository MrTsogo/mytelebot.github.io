from telebot.types import ReplyKeyboardMarkup, KeyboardButton

_button = KeyboardButton("Цены")

prices_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
prices_markup.add(_button)
