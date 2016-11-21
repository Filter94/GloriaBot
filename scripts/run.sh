#!/usr/bin/env bash
. telegram_bot/bin/activate
gunicorn -b 127.0.0.1:5000 --reload --log-file gunicorn.log -p pid -w 1 gloria_bot.runserver:app -D
deactivate
