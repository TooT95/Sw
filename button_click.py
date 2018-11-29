import telebot
from telebot import types
from Work import Work_with_file, config,Main_part
from PIL import Image

bot = telebot.TeleBot(config.token)

current_command = ""

@bot.message_handler(commands=["start"])
def commands(message):
    bot.send_message(message.chat.id,"Приветствуем!")

@bot.message_handler(commands=["test"])
def commands(message):
    current_command = str(message.text).replace("/","")
    Work_with_file.write_in_command(current_command)
    Main_part.set_commands(bot,current_command,message)

@bot.message_handler(commands=["picture"])
def commands(message):
    current_command = str(message.text).replace("/","")
    Work_with_file.write_in_command(current_command)
    Main_part.set_commands(bot, current_command, message)

@bot.message_handler(commands=["listening"])
def commands(message):
    current_command = str(message.text).replace("/","")
    Work_with_file.write_in_command(current_command)
    Main_part.set_commands(bot, current_command, message)



@bot.message_handler(func=lambda message: True,content_types=['text'])
def handle_message(message):
    Main_part.check_types_messages(bot,message)

if __name__ == '__main__':
    bot.polling(none_stop=True)
