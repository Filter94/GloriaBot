# -*- coding: utf-8 -*-
from unittest import TestCase
from mock import patch
import json

patch('telegram.bot.Bot.get_me', return_value="Me").start()
patch('telegram.bot.Bot.getMe', return_value="Me").start()

from gloria_bot import runserver


class GloriaTest(TestCase):
    API_PATH = '/'
    SIMPLE_PRIVATE_MESSAGE = {
        "update_id": 1,
        "message": {
            "message_id": 1,
            "from": {
                "id": 1,
                "first_name": "Test",
                "last_name": "Test"
            },
            "chat": {
                "id": 1,
                "first_name": "Test",
                "last_name": "Test",
                "type": "private"
            },
            "date": 1,
            "text": ""
        }
    }

    def setUp(self):
        self.app = runserver.app.test_client()

    def send_json(self, dict):
        return self.app.post(self.API_PATH, data=json.dumps(dict),
                             content_type='application/json')
