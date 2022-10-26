import telebot
import random
import os

bot = telebot.TeleBot('5797605402:AAHHmMrwPZgAFKvO065meCrVvltWf4IG7ko')
counter = 0
print("Bot started...")


@bot.message_handler(commands=["start"])
def start_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Привет! Добро пожаловать в мой уютный телеграм бот! ^^")


@bot.message_handler(commands=["help"])
def help_message(message):
    bot.reply_to(message, "Напиши слово \"фото\" и бот пришлет тебе семейную фотографию!")


@bot.message_handler(content_types=["text"])
def send_message(message):
    chat_id = message.chat.id
    text = message.text.lower()
    global counter
    counter += 1
    print(str(counter) + '. ' + text)
    if text in ("привет", "hi", "hello"):
        bot.send_message(chat_id, "Дратути!")
    elif text == "фото":
        bot.send_photo(chat_id, open('/home/swap/Downloads/bot_photos/' + random.choice(os.listdir('/home/swap/Downloads/bot_photos/')), 'rb'))
    else:
        bot.send_message(chat_id, "Моя твоя не понимать!")


bot.polling()
