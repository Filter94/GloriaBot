# -*- coding: utf-8 -*-
from mock import patch, Mock

# No network interactions
from gloria_bot.singletons import bot
from tests.gloria_test import GloriaTest


class TestSmoke(GloriaTest):
    @patch('telegram.bot.Bot.send_message', autospec=True)
    def test_start(self, send_message_mock):
        start_dict = self.SIMPLE_PRIVATE_MESSAGE
        start_dict['message']['text'] = '/start'
        response = self.send_json(start_dict)
        self.assertEqual(response.status_code, 200)
        send_message_mock.assert_called_once_with(bot, 1, u'Утро.')

    @patch('telegram.bot.Bot.send_message', new_callable=Mock())
    def test_usual_message(self, send_message_mock):
        self.perform_test_with_message(u'Случайное сообщение', times=6)
        try:
            send_message_mock.assert_not_called()
        except AssertionError as ae:
            print send_message_mock.all_calls
            raise ae
