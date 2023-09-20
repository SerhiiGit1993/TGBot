import telebot
from telebot import types
import time

from local import *
from youtube import send_latest_videos, send_random_videos

bot = telebot.TeleBot(BOT_TOKEN)

button_click_times = {}


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Щойно вийшло")
    button2 = types.KeyboardButton("Рандомне відео")
    button3 = types.KeyboardButton("Що нового у автора")
    button4 = types.KeyboardButton("На каву")
    button5 = types.KeyboardButton("Затишний чат без бану і ненависті")
    keyboard.add(button1, button2, button3, button4, button5)

    bot.send_message(message.chat.id, WELCOME_TEXT, reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    text = message.text
    user_id = message.from_user.id

    last_click_time = button_click_times.get(user_id, 0)
    current_time = time.time()

    if current_time - last_click_time >= 1:
        button_click_times[user_id] = current_time
        match text:
            case "Щойно вийшло":
                send_latest_videos(message)
            case "Рандомне відео":
                send_random_videos(message)
            case "Що нового у автора":
                bot.send_message(message.chat.id, f"Дізнайся тут:\n{LIFE_CHANNEL}")
            case "Затишний чат без бану і ненависті":
                bot.send_message(message.chat.id, f"Спілкуйся тут:\n{TALK_CHANNEL}")
            case "На каву":
                bot.send_message(message.chat.id, f"Закинь тут:\n{DONATE}")
            case _:
                bot.send_message(message.chat.id, "Не вдалось розпізнати команду")
    else:
        bot.send_message(message.chat.id, "Будь ласка, зачекайте ще трохи перед наступним натисканням кнопки.")


if __name__ == '__main__':
    bot.polling(none_stop=True)
