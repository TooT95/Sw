import os
import time
import telebot
from random import randint
from flask import Flask, request
from constants import *

bot = telebot.TeleBot(token)
server = Flask(__name__)


def get_task_by_number(tasks, number):
    try:
        return next((x for x in tasks if x.number == number), None)
    except:
        return None


def get_random_task(tasks):
    rand = randint(1, len(tasks))
    if 1 <= rand <= len(tasks):
      return get_task_by_number(tasks, rand)
    else:
      return None


@bot.message_handler(commands=['start'])
def start(message):
    text_of_message = start_command_message
    bot.send_message(message.from_user.id, text_of_message)

@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://8d4e993f.ngrok.io/' + token)
    return "!", 200


if __name__ == "__main__":
    server.debug = True
    server.run()
