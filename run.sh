#!/usr/bin/env bash
. telegram_bot/bin/activate
gunicorn -b 127.0.0.1:5000 --reload --log-file gunicorn.txt -p pid -w 1 runserver:app -D
