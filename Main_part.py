import telebot
from telebot import types
from Work import Work_with_file
from PIL import Image


def check_types_messages(bot,message):
    current_command = Work_with_file.open_files_command()
    if current_command == 'test':
        if (message.text == '10'):
            bot.send_message("500324557", "Right")
        else:
            bot.send_message("500324557", "!")
    else:
        if (message.text == 'has'):
            bot.send_message("500324557", "Right")
        else:
            bot.send_message("500324557", "!")

def set_commands(bot,current_command,message):
    if (current_command == "test"):
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        button_1 = types.KeyboardButton(text="10")
        button_2 = types.KeyboardButton(text="11")
        keyboard.add(button_1, button_2)
        # keyboard = types.InlineKeyboardButton("F u",url="")
        bot.send_message(message.chat.id, "5+5", reply_markup=keyboard)
    elif (current_command == "picture"):
        keyboard = types.ReplyKeyboardMarkup(row_width=3)
        button_1 = types.KeyboardButton(text="have")
        button_2 = types.KeyboardButton(text="has")
        button_3 = types.KeyboardButton(text="are")
        keyboard.add(button_1, button_2, button_3)
        with open("2.jpg",'rb') as photo:
            bot.send_photo(message.chat.id, photo, reply_markup=keyboard)
    elif (current_command == "listening"):
        with open('1.mp3','rb') as file:
            bot.send_audio(message.chat.id,file)
    else:
        bot.send_message(message.chat.id, "Choose other command")