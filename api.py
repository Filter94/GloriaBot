# Process webhook calls
import flask

import telebot
from runserver import WEBHOOK_URL_PATH, bot, app


@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().encode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        telebot.logger.debug(json_string)
        bot.process_new_messages([update.message])
        return ''
    else:
        flask.abort(403)


# Empty webserver index, return nothing, just http 200
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return ''
