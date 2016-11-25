# -*- coding: utf-8 -*-
from mock import patch, call

# No network interactions
from gloria_bot.singletons import bot
from tests.gloria_test import GloriaTest


class TestPidors(GloriaTest):
    REPEAT = 20

    def perform_test_with_message(self, message):
        kalinin_pidor_dict = dict(self.SIMPLE_PRIVATE_MESSAGE)
        kalinin_pidor_dict['message']['text'] = message
        for i in range(self.REPEAT):
            # Probability of test failing is 1/2^10
            response = self.send_json(self.SIMPLE_PRIVATE_MESSAGE)
            self.assertEqual(response.status_code, 200)

    @patch('telegram.bot.Bot.send_message', autospec=True)
    def test_kalinin(self, send_message_mock):
        self.perform_test_with_message(u'Калинин')
        send_message_mock.assert_has_calls([call(bot, 1, u'Калинин пидор')])

    @patch('telegram.bot.Bot.send_message', autospec=True)
    def test_kalinin_contains(self, send_message_mock):
        self.perform_test_with_message(u'Щас бы Калинина увидеть')
        send_message_mock.assert_has_calls([call(bot, 1, u'Калинин пидор')])

    @patch('telegram.bot.Bot.send_message', autospec=True)
    def test_stas(self, send_message_mock):
        self.perform_test_with_message(u'Стас')
        send_message_mock.assert_has_calls([call(bot, 1, u'Стас по дефолту пидор')])

    @patch('telegram.bot.Bot.send_message', autospec=True)
    def test_stas_contains(self, send_message_mock):
        self.perform_test_with_message(u'Щас бы Стаса увидеть')
        send_message_mock.assert_has_calls([call(bot, 1, u'Стас по дефолту пидор')])

    @patch('telegram.bot.Bot.send_message', autospec=True)
    def test_tema(self, send_message_mock):
        self.perform_test_with_message(u'Тема')
        send_message_mock.assert_has_calls([call(bot, 1, u'Да и Тема пидор')])

    @patch('telegram.bot.Bot.send_message', autospec=True)
    def test_tema_contains(self, send_message_mock):
        self.perform_test_with_message(u'Щас бы Артема увидеть')
        send_message_mock.assert_has_calls([call(bot, 1, u'Да и Тема пидор')])

    @patch('telegram.bot.Bot.send_message', autospec=True)
    def test_albert(self, send_message_mock):
        self.perform_test_with_message(u'Альберт')
        send_message_mock.assert_has_calls([call(bot, 1, u'Альберт тоже пидор')])

    @patch('telegram.bot.Bot.send_message', autospec=True)
    def test_albert_contains(self, send_message_mock):
        self.perform_test_with_message(u'Щас бы Альберта увидеть')
        send_message_mock.assert_has_calls([call(bot, 1, u'Альберт тоже пидор')])

    @patch('telegram.bot.Bot.send_message', autospec=True)
    def test_geva(self, send_message_mock):
        self.perform_test_with_message(u'Гева')
        send_message_mock.assert_has_calls([call(bot, 1, u'Гева дизайнер')])

    @patch('telegram.bot.Bot.send_message', autospec=True)
    def test_geva_contains(self, send_message_mock):
        self.perform_test_with_message(u'Щас бы Геворка увидеть')
        send_message_mock.assert_has_calls([call(bot, 1, u'Гева дизайнер')])
