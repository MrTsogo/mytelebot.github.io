from threading import Thread
from datetime import datetime
from telebot import TeleBot
import time

from scraper import check_price
from config import API_TOKEN
from markups import prices_markup

bot = TeleBot(token=API_TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    if message.chat.id == 2082545869:
        bot.send_message(2082545869, "Доброго времени суток, Михаил.\nБот запущен.", reply_markup=prices_markup)
    else:
        bot.send_message(message.chat.id, f"Это частный бот, который работает только с его владельцем")


@bot.message_handler(content_types=["text"])
def send_prices(message):
    if message.text.lower() in ["цены", "/prices"] and message.chat.id == 2082545869:
        bot.send_message(2082545869, "Пожалуйста, подождите...")
        
        prices = "\n".join(check_price())

        
        bot.delete_message(2082545869, message.message_id + 1)
        bot.send_message(2082545869, prices, reply_markup=prices_markup)
    elif message.chat.id != 2082545869:
        start_message(message=message)
    else:
        bot.send_message(2082545869, f"Команда {message.text} не распознана.", reply_markup=prices_markup)


def auto_send_prices(bot):
    while True:
        n = [datetime.now().hour, datetime.now().minute, datetime.now().second]
        if n == [16, 0, 0] or n == [11, 0, 0]:
            prices = "\n".join(check_price())
            bot.send_message(2082545869, prices, reply_markup=prices_markup)
        time.sleep(10)
      

if __name__ == "__main__":
    Thread(target=auto_send_prices, args=(bot,)).start()
    bot.infinity_polling()
