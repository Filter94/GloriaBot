import telebot
from const import API_TOKEN

bot = telebot.TeleBot(API_TOKEN, threaded=False)
