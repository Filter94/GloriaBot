# -*- coding: utf-8 -*-
from mock import patch

# No network interactions
from gloria_bot.singletons import bot
from tests.gloria_test import GloriaTest


class TestStart(GloriaTest):
    @patch('telegram.bot.Bot.send_message', autospec=True)
    def test_start(self, send_message_mock):
        start_dict = self.SIMPLE_PRIVATE_MESSAGE
        start_dict['message']['text'] = '/start'
        response = self.send_json(start_dict)
        self.assertEqual(response.status_code, 200)
        send_message_mock.assert_called_once_with(bot, 1, u'Утро.')
