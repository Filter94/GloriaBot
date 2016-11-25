import flask
from telegram.bot import Bot
from telegram.ext import Updater

from api_token import API_TOKEN

bot = Bot(API_TOKEN)
app = flask.Flask(__name__)
updater = Updater(bot=bot)
# Get the dispatcher to register handlers
dp = updater.dispatcher
