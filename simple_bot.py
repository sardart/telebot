# Very simple Telegram Bot
# Created by Artur Sardaryan

import telebot

# Your API Token from BotFather
API_TOKEN = '123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi'

# Creating Telebot object
bot = telebot.TeleBot(API_TOKEN)


# Handler for commands (example: /start)
@bot.message_handler(commands=['start'])
def start(message):
    answer = "Hello World"
    bot.send_message(chat_id=message.chat.id, text=answer)


# Handler for messages with content_type 'text'
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    # Reply to the sender with the same text
    bot.reply_to(message, message.text)


# Allows the bot to retrieve updates and notify handlers.
bot.polling()
