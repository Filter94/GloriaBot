#!/usr/bin/env python
# -*- coding: utf-8 -*-
import flask
import telebot
import logging

import handlers
from bot import bot
import const

handlers.init()

logging.basicConfig(filename='loggers.log', level=logging.DEBUG)

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

app = flask.Flask(__name__)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, u"Утро.")


@app.route(const.WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().encode('utf-8')
        telebot.logger.debug(flask.request.get_data())
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_messages([update.message])
        return ''
    else:
        flask.abort(403)


# Empty webserver index, return nothing, just http 200
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return ''


if __name__ == '__main__':
    # Remove webhook, it fails sometimes the set if there is a previous webhook
    bot.remove_webhook()
    # Set webhook
    bot.set_webhook(url=const.WEBHOOK_URL_BASE + const.WEBHOOK_URL_PATH,
                    certificate=open(const.WEBHOOK_SSL_CERT, 'r'))
    # Start flask server
    app.run(host=const.WEBHOOK_LISTEN,
            port=const.WEBHOOK_PORT,
            ssl_context=(const.WEBHOOK_SSL_CERT, const.WEBHOOK_SSL_PRIV))
