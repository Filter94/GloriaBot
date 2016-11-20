#!/usr/bin/env bash
git pull origin master
. telegram_bot/bin/activate
pip install -r requirements.txt