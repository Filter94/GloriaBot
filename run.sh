#!/usr/bin/env bash
. telegram_bot/bin/activate
gunicorn -b 0.0.0.0:8443 --reload --keyfile webhook_pkey.pem --certfile webhook_cert.pem --log-file gunicorn.txt -p pid -w 1 runserver:app -D
