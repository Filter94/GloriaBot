#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import flask

import handlers
import telebot
from bot import bot

logging.basicConfig(filename='loggers.log', level=logging.DEBUG)

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

handlers.init()

app = flask.Flask(__name__)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, u"Утро.")


@app.route('/', methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().encode('utf-8')
        telebot.logger.debug(flask.request.get_data())
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_messages([update.message])
        return ''
    else:
        flask.abort(403)


if __name__ == '__main__':
    # Start flask server
    app.run()
