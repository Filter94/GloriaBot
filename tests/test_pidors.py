# -*- coding: utf-8 -*-
from mock import patch, call

from gloria_bot.singletons import bot
from tests.gloria_test import GloriaTest


class TestPidors(GloriaTest):
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
