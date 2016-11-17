#!/usr/bin/env bash
. telegram_bot/bin/activate
gunicorn -b 0.0.0.0:8443 --preload --keyfile webhook_pkey.pem --certfile webhook_cert.pem -p pid -w 1 runserver:app -D
