# Reply Keyboard Markup Example
# Created by Artur Sardaryan

import telebot
from telebot import types

# Your API Token from BotFather
API_TOKEN = '123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi'

# Creating Telebot object
bot = telebot.TeleBot(API_TOKEN)


# Handler for commands (example: /start)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('First Button', 'Second Button')
    markup.row('Third Button')

    answer = "Hi!"
    bot.send_message(chat_id=message.chat.id, text=answer, reply_markup=markup)


# Handler for messages with content_type 'text'
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    msg = message.text
    answer = "Default answer"

    if msg == "First Button":
        # do something
        answer = "You tapped frist button"
    elif msg == "Second Button":
        # do something
        answer = "You tapped second button"
    elif msg == "Third Button":
        # do something
        answer = "You tapped third button"

    bot.send_message(chat_id=message.chat.id, text=answer)


# Allows the bot to retrieve updates and notify handlers.
bot.polling()