# coding=utf-8
import logging

import sys

logger = logging.getLogger(__name__)


def exceptions_handler(type, value, tb):
    logger.debug("Uncaught exception: {0}".format(str(value)))


sys.excepthook = exceptions_handler


def kalinin_pidor(bot, update):
    bot.send_message(update.chat_id, u'Калинин пидор')


def albert_pidor(bot, update):
    bot.send_message(update.chat_id, u'Альберт тоже пидор')


def tema_pidor(bot, update):
    bot.send_message(update.chat_id, u'Да и Тема пидор')


def geva_pidor(bot, update):
    bot.send_message(update.chat_id, u'Гева дизайнер')


def stas_pidor(bot, update):
    bot.send_message(update.chat_id, u'Стас по дефолту пидор')


def ban(bot, update):
    bot.send_message(update.chat_id, u'Бан')
    try:
        bot.kick_chat_member(update.chat_id, update.message.user.id)
    except Exception:
        pass


def net(bot, update):
    net_file_id = "BQADAgADCQADSXzJD8TFvW03Uai0Ag"
    bot.send_sticker(update.message.chat_id, net_file_id)


def debug(bot, update):
    bot.send_message(update.chat_id, u'Стас по дефолту пидор')


def error(bot, update, error):
    logger.error('Update "%s" caused error "%s"' % (update, error))


nicknames_dict = {
    u'Vaseev': u'Рома',
    u'Kalinin': u'Калинин',
    u'Hoffner': u'Альберт',
    u'Sten': u'Стас',
    u'Georgienko': u'Хома',
    u'Молчанов': u'Тёма',
    u'Rueda': u'Роб',
    u'Бафомет': u'Валя',
    None: u'Гева'
}


def zaebal(bot, update):
    try:
        name = nicknames_dict.get(update.message.from_user.last_name, update.message.from_user.first_name)
        bot.send_message(update.chat_id, u'%s, как ты заебал!(' % name)
    except Exception as e:
        print(e.message)
        try:
            print(update.message.from_user.last_name)
        except Exception:
            pass


def morning(bot, update):
    bot.send_message(update.chat_id, u'Утро.')


def night(bot, update):
    bot.send_message(update.chat_id, u'Ночи.')


def sex(bot, update):
    sex_sticker_file_id = "BQADAgADDwADSXzJDy9IYTmxdYnWAg"
    bot.send_sticker(update.message.chat_id, sex_sticker_file_id)


def start(bot, update):
    bot.send_message(update.chat_id, u'Утро.')
