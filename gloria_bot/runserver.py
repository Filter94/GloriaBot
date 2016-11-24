#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import flask
import json
from telegram import Update
from telegram.ext import CommandHandler

from gloria_bot import callbacks
from gloria_bot.handlers.regex_probability_handler import RegexProbabilityHandler
from gloria_bot.handlers.zaebal_handler import ZaebalHandler
from gloria_bot.singletons import dp, app, updater, bot

UTF_8 = "utf-8"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='loggers.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)


@app.route('/', methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().encode(UTF_8)
        logger.debug(flask.request.get_data())
        update_dict = json.loads(json_string, encoding=UTF_8)
        update = Update.de_json(update_dict, bot)
        updater.dispatcher.process_update(update)
        logger.debug("Update is processed.")
        return ''
    else:
        flask.abort(403)

# add all handlers
dp.add_handler(CommandHandler('start', callbacks.start))
dp.add_handler(ZaebalHandler(ur'.*', callbacks.zaebal, 0.9))
dp.add_handler(RegexProbabilityHandler(ur'(?iu).*калинин.*', callbacks.kalinin_pidor, 0.5))
dp.add_handler(RegexProbabilityHandler(ur'(?iu).*нет[!?.)(]*$', callbacks.net, 0.7))
dp.add_handler(RegexProbabilityHandler(ur'(?iu).*альберт.*', callbacks.albert_pidor, 0.5))
dp.add_handler(RegexProbabilityHandler(ur'(?iu).*(тема|тёма|артем).*', callbacks.tema_pidor, 0.5))
dp.add_handler(RegexProbabilityHandler(ur'(?iu).*(гева|геворг|геворк).*', callbacks.geva_pidor, 0.5))
dp.add_handler(RegexProbabilityHandler(ur'(?iu).*(стас|пидорас|пидор).*', callbacks.stas_pidor, 0.5))
dp.add_handler(RegexProbabilityHandler(ur'debug', callbacks.debug))
dp.add_handler(RegexProbabilityHandler(ur'(?iu).*(на ?хуй|в пизду|впизду),? глория.*', callbacks.ban, 0.9))
dp.add_handler(RegexProbabilityHandler(ur'(?iu)(.{0,6}|добр{0,6})\s?(прив|утр[оа]).{0,20}', callbacks.morning, 0.9))
dp.add_handler(RegexProbabilityHandler(ur'(?iu)(.{0,10}|добр{0,10})\s?ночи.{0,20}', callbacks.night, 0.9))
dp.add_handler(RegexProbabilityHandler(ur'(?iu).*(трахать|ебать|секс).*', callbacks.sex, 0.9))
dp.add_handler(RegexProbabilityHandler(ur'(?iu).*( еда+| (по)?ку+шать | (по)?ку+шаю| (по)?ку+шал | (по)?е+м |'
                                       ur' (по)?ха+ваю | (по)?ха+вать | (по)?ха+вал | (по)?е+сть | (по)?е+л | вку+сн | ня+м ).*',
                                       callbacks.eat, 0.9))
# log all errors
dp.add_error_handler(callbacks.error)

# Open tcp connection to avoid poor performance on the very first query
bot_user = bot.getMe()
assert bot_user is not None

if __name__ == '__main__':
    # Start flask server
    app.run()
