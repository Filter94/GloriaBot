import flask
from telegram.utils.request import Request
from telegram.bot import Bot
from telegram.ext import Updater

from api_token import API_TOKEN

request = Request(con_pool_size=10)
bot = Bot(API_TOKEN, request=request)
app = flask.Flask(__name__)
updater = Updater(bot=bot)
# Get the dispatcher to register handlers
dp = updater.dispatcher
