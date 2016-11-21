import telebot
from api_token import API_TOKEN

bot = telebot.TeleBot(API_TOKEN, threaded=False)
