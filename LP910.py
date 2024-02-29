import traceback
import sqlite3
from telebot import types
from telegram import ParseMode
import datetime
import urllib.request
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os
import openai
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Update
import time
import json
import openpyxl
from datetime import datetime, timedelta
from telegram import InputFile
import schedule
import time
import telebot
import requests
from requests import post
import fake_useragent
from bs4 import BeautifulSoup

CHAT_ID = 628446966
TELEGRAM_API_KEY = '6836641537:AAFdhGC-3j9g0hJamPrUhZr8BHHPLobs4qQ'
bot = telebot.TeleBot(TELEGRAM_API_KEY)


def get_user_data(user_id):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute(f"SELECT id, username FROM login_id WHERE id = {user_id}")
    data = cursor.fetchone()
    return data


@bot.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('alibase.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id (
            id             INTEGER,
            username       TEXT)""")
    username = message.chat.username
    user_id = message.chat.id
    user_data = get_user_data(user_id)
    if user_data is not None:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Групові заняття'))
        markup.add(types.KeyboardButton('Cкасувати запис на тренування'))
        markup.add(types.KeyboardButton('Послуги тренера'))
        markup.add(types.KeyboardButton('Заморозити абонемент'))
        markup.add(types.KeyboardButton('Дізнатися про стан абонементу'))
        markup.add(types.KeyboardButton("Зв'язок з дирекцією"))
        markup.add(types.KeyboardButton('Замовити страви'))
        markup.add(types.KeyboardButton('Хочу працювати в Алігаторі'))
        bot.send_message(message.chat.id, f"Оберіть функцію із кнопок", reply_markup=markup)
        bot.register_next_step_handler(message, All.branching)

    else:
        cursor.execute(
            "INSERT INTO login_id (id, username) VALUES (?,?);",(user_id,username))
        connect.commit()
        connect.close()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Групові заняття'))
        markup.add(types.KeyboardButton('Cкасувати запис на тренування'))
        markup.add(types.KeyboardButton('Послуги тренера'))
        markup.add(types.KeyboardButton('Заморозити абонемент'))
        markup.add(types.KeyboardButton('Дізнатися про стан абонементу'))
        markup.add(types.KeyboardButton("Зв'язок з дирекцією"))
        markup.add(types.KeyboardButton('Замовити страви'))
        markup.add(types.KeyboardButton('Хочу працювати в Алігаторі'))
        bot.send_message(message.chat.id, f"Оберіть функцію із кнопок", reply_markup=markup)
        bot.register_next_step_handler(message, All.branching)

class All:
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def branching(message):
        text = message.text
        if text == "Групові заняття":
            pass
        elif text == "Cкасувати запис на тренування":
            pass
        elif text == "Послуги тренера":
            pass
        elif text == "Заморозити абонемент":
            pass
        elif text == "Дізнатися про стан абонементу":
            pass
        elif text == "Зв'язок з дирекцією":
            pass
        elif text == "Замовити страви":
            pass
        elif text == "Дізнатися про стан абонементу":
            pass
        elif text == "Хочу працювати в Алігаторі":
            pass
        else:
            pass


#групові заняття
class Group_classes:
    def __init__(self, bot):
        self.bot = bot


#скасувати запис на тренування
class Cancel:
    def __init__(self, bot):
        self.bot = bot

#послуги тренера
class Coach_services:
    def __init__(self, bot):
        self.bot = bot



#Заморозити абонемент
class Freeze:
    def __init__(self, bot):
        self.bot = bot

#Дізнатися про стан абонементу
class Status_subscription:
    def __init__(self, bot):
        self.bot = bot




#Зв'язатися з дирекцією комплексу
class Contact:
    def __init__(self, bot):
        self.bot = bot




#Замовити страви
class Order_meals:
    def __init__(self, bot):
        self.bot = bot

#Хочу працювати в Алігаторі
class Work:
    def __init__(self, bot):
        self.bot = bot





while True:
    try:
        bot.polling(none_stop=True, skip_pending=True)
    except Exception as e:
        bot.send_message(CHAT_ID, f"Помилка: {e}\n\n{traceback.format_exc()}")

