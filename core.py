import telebot
from telebot import types

from local import *
from youtube import send_latest_videos

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Не лінись і підпишись")
    button2 = types.KeyboardButton("Нове відео на каналі")
    button3 = types.KeyboardButton("Що нового у автора")
    button4 = types.KeyboardButton("На каву")
    button5 = types.KeyboardButton("Затишний чат без бану і ненависті")
    keyboard.add(button1, button2, button3, button4, button5)

    bot.send_message(message.chat.id, WELCOME_TEXT, reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    text = message.text
    match text:
        case "Не лінись і підпишись":
            bot.send_message(message.chat.id, "Ви натиснули Кнопку 1")
        case "Нове відео на каналі":
            send_latest_videos(message)
        case "Що нового у автора":
            bot.send_message(message.chat.id, f"Дізнайся тут:\n{LIFE_CHANNEL}")
        case "Затишний чат без бану і ненависті":
            bot.send_message(message.chat.id, f"Спілкуйся тут:\n{TALK_CHANNEL}")
        case "На каву":
            bot.send_message(message.chat.id, f"Закинь тут:\n{DONATE}")
        case _:
            bot.send_message(message.chat.id, "Не вдалось розпізнати команду")


bot.polling(none_stop=True)
