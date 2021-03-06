# coding=utf-8
import logging

import sys
import random

from gloria_bot.youtube_search import youtube_search

YOUTUBE_LINK = 'youtube.com/watch?v=%s'

logger = logging.getLogger(__name__)


def exceptions_handler(type, value, tb):
    logger.debug("Uncaught exception: {0}".format(str(value)))


sys.excepthook = exceptions_handler


def kalinin_pidor(bot, update):
    bot.send_message(update.message.chat_id, u'Калинин пидор')


def albert_pidor(bot, update):
    bot.send_message(update.message.chat_id, u'Альберт тоже пидор')


def tema_pidor(bot, update):
    bot.send_message(update.message.chat_id, u'Да и Тема пидор')


def geva_pidor(bot, update):
    bot.send_message(update.message.chat_id, u'Гева дизайнер')


def stas_pidor(bot, update):
    bot.send_message(update.message.chat_id, u'Стас по дефолту пидор')


def ban(bot, update):
    bot.send_message(update.message.chat_id, u'Бан')
    try:
        bot.kick_chat_member(update.chat_id, update.message.user.id)
    except Exception:
        pass


def net(bot, update):
    net_file_id = "BQADAgADCQADSXzJD8TFvW03Uai0Ag"
    bot.send_sticker(update.message.chat_id, net_file_id)


def debug(bot, update):
    bot.send_message(update.message.chat_id, u'Стас по дефолту пидор')


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
        bot.send_message(update.message.chat_id, u'%s, как ты заебал!(' % name)
    except Exception as e:
        print(e.message)
        try:
            print(update.message.from_user.last_name)
        except Exception:
            pass


def morning(bot, update):
    bot.send_message(update.message.chat_id, u'Утро.')


def night(bot, update):
    bot.send_message(update.message.chat_id, u'Ночи.')


def sex(bot, update):
    sex_sticker_file_id = "BQADAgADDwADSXzJDy9IYTmxdYnWAg"
    bot.send_sticker(update.message.chat_id, sex_sticker_file_id)


def start(bot, update):
    bot.send_message(update.message.chat_id, u'Утро.')


def eat(bot, update):
    eat_gif_file_id = "BQADBAADLwMAAg0eZAclqTS6xDhUVQI"
    bot.send_document(update.message.chat_id, eat_gif_file_id)


def get_first_video_or_say(keyword, reply, bot, update):
    search_result = youtube_search(keyword)
    if search_result:
        try:
            video_id = search_result[0]
            bot.send_message(update.message.chat_id, YOUTUBE_LINK % video_id)
        except Exception as e:
            logger.info("Can't handle %s" % keyword)
            logger.info("Youtube search result: %s" % search_result)
    else:
        bot.send_message(update.message.chat_id, reply)


def get_some_video_or_say(keyword, reply, bot, update):
    search_result = youtube_search(keyword)
    if search_result:
        try:
            video_id = random.choice(search_result)
            bot.send_message(update.message.chat_id, YOUTUBE_LINK % video_id)
        except Exception as e:
            logger.info("Can't handle %s" % keyword)
            logger.info("Youtube search result: %s" % search_result)
    else:
        bot.send_message(update.message.chat_id, reply)


VIDEO_TYPE_RESPONSES = {
    u"видео": u"Какое видео, блять?",
    u"ролик": u"Какой ролик, блять?",
    u"видос": u"Какой видос, блять?"
}


def search_video_about(bot, update, groupdict=None):
    if groupdict is None:
        groupdict = dict()
    keyword = groupdict['keyword']
    if keyword == '':
        bot.send_message(update.message.chat_id, VIDEO_TYPE_RESPONSES[groupdict['video_type']])
        return
    get_first_video_or_say(keyword, u'Не бывает про %s видео.' % keyword, bot, update)


def search_video(bot, update, groupdict=None):
    if groupdict is None:
        groupdict = dict()
    keyword = groupdict['keyword']
    if keyword == '':
        bot.send_message(update.message.chat_id, VIDEO_TYPE_RESPONSES[groupdict['video_type']])
        return
    get_first_video_or_say(keyword, u'Не бывает видео "%s".' % keyword, bot, update)


def search_some_video_about(bot, update, groupdict=None):
    if groupdict is None:
        groupdict = dict()
    keyword = groupdict['keyword']
    if keyword == '':
        bot.send_message(update.message.chat_id, VIDEO_TYPE_RESPONSES[groupdict['video_type']])
        return
    get_some_video_or_say(keyword, u'Не бывает про %s никаких видео.' % keyword, bot, update)


def search_some_video(bot, update, groupdict=None):
    if groupdict is None:
        groupdict = dict()
    keyword = groupdict['keyword']
    if keyword == '':
        bot.send_message(update.message.chat_id, VIDEO_TYPE_RESPONSES[groupdict['video_type']])
        return
    get_some_video_or_say(keyword, u'Не бывает никаких видео "%s".' % keyword, bot, update)

