# Dialog Telegram Bot
# Created by Artur Sardaryan

import telebot
import random

# Your API Token from BotFather
API_TOKEN = '123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi'

# Creating Telebot object
bot = telebot.TeleBot(API_TOKEN)

# You can load this dialogs from file or from anywhere else
dialogs = {
    "Hello": ["Hi!", "Howdy", "Hey", "Hello", "Yo!", "What’s up?"],
    "How are you?": ["I am fine! And you?", "Boredom", "I'm good"],
    "What is your name?": ["Jarvis", "Siri", "Alice", "Justin", "Sonny", "Ultron", "Vision"],
    "How old are you?": ["18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
}

default_answers = [
    "Build your own dreams, or someone else will hire you to build theirs",
    "Fall seven times and stand up eight",
    "There are no shortcuts to any place worth going",
    "Remember no one can make you feel inferior without your consent",
    "You only live once, but if you do it right, once is enough",
    "Learning is a treasure that will follow its owner everywhere",
    "Knowledge is power"
]


def generate_random_answer(incoming_message):
    if incoming_message in dialogs:
        answers = dialogs[incoming_message]
        return random.choice(answers)
    else:
        return random.choice(default_answers)


# Handler for start command
@bot.message_handler(commands=['start'])
def start(message):
    answer = "Hi, let's chat!"
    bot.send_message(chat_id=message.chat.id, text=answer)


# Handler for messages with content_type 'text'
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    incoming_message = message.text
    full_name = "%s %s" % (message.from_user.first_name, message.from_user.last_name)

    answer = generate_random_answer(incoming_message)
    bot.send_message(chat_id=message.chat.id, text=answer)

    # display dialog in the console
    print("%s: %s" % (full_name, incoming_message))
    print("Bot: %s\n" % answer)


# Allows the bot to retrieve updates and notify handlers.
bot.polling()
