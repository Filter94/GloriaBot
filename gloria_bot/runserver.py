#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import flask
import json
from telegram import Update

from gloria_bot.handlers_init import init_handlers
from gloria_bot.singletons import app, updater, bot, request

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
        logger.debug("Connection pool size: %s" % len(request.__dict__['_con_pool'].pools.__dict__['_container']))
        logger.debug("Update %s processing started." % update.update_id)
        updater.dispatcher.process_update(update)
        logger.debug("Update %s is processed." % update.update_id)
        return ''
    else:
        flask.abort(403)

# Open tcp connection to avoid poor performance on the very first query
bot_user = bot.get_me()
assert bot_user is not None

init_handlers()

if __name__ == '__main__':
    # Start flask server
    app.run()
