import telebot
from telebot import types

from local import *

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Кнопка 1")
    button2 = types.KeyboardButton("Кнопка 2")
    keyboard.add(button1, button2)

    bot.send_message(message.chat.id, WELCOME_TEXT, reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    text = message.text
    match text:
        case "Кнопка 1":
            bot.send_message(message.chat.id, "Ви натиснули Кнопку 1")
        case "Кнопка 2":
            bot.send_message(message.chat.id, "Ви натиснули Кнопку 2")
        case _:
            bot.send_message(message.chat.id, "Не вдалось розпізнати команду")


bot.polling(none_stop=True)
