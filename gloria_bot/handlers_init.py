#!/usr/bin/env python
# -*- coding: utf-8 -*-
# add all handlers
import logging
from telegram.ext import CommandHandler
from telegram.ext import RegexHandler

from gloria_bot import callbacks
from gloria_bot.handlers.regex_probability_handler import RegexProbabilityHandler
from gloria_bot.handlers.zaebal_handler import ZaebalHandler
from gloria_bot.singletons import dp

logger = logging.getLogger(__name__)


def init_handlers():
    statement_start = u"([ .!?)(]|^)"
    statement_end = u"([ $.!?)(]|$)"
    statement_delimiter = statement_end + u"*|" + statement_start + u"*"
    eat_words = [u"еда+", u"(по)?ку+шать", u"(по)?ку+шаю", u"(по)?ку+шал(а)?",
                 statement_start + u"(по)?е+м" + statement_end, u"(по)?ха+ваю", u"(по)?ха+вать", u"(по)?ха+вал(а)?",
                 statement_start + u"(по)?е+л(а)?" + statement_end, u"вку+сн", u"ня+м", u"ня+мка+"]
    eat_choice = statement_start + statement_delimiter.join(eat_words) + statement_end

    dp.add_handler(CommandHandler('start', callbacks.start))
    dp.add_handler(ZaebalHandler(ur'.*', callbacks.zaebal, 0.9))
    dp.add_handler(RegexProbabilityHandler(ur'(?iu).*калинин.*', callbacks.kalinin_pidor, 0.5))
    dp.add_handler(RegexProbabilityHandler(ur'(?iu).*нет%s*$' % statement_end, callbacks.net, 0.7))
    dp.add_handler(RegexProbabilityHandler(ur'(?iu).*альберт.*', callbacks.albert_pidor, 0.5))
    dp.add_handler(RegexProbabilityHandler(ur'(?iu).*(тема|тёма|артем).*', callbacks.tema_pidor, 0.5))
    dp.add_handler(RegexProbabilityHandler(ur'(?iu).*(гева|геворг|геворк).*', callbacks.geva_pidor, 0.5))
    dp.add_handler(RegexProbabilityHandler(ur'(?iu).*(стас|пидорас|пидор).*', callbacks.stas_pidor, 0.5))
    dp.add_handler(RegexHandler(ur'debug', callbacks.debug))
    dp.add_handler(RegexProbabilityHandler(ur'(?iu).*(на ?хуй|в пизду|впизду),? глория.*', callbacks.ban, 0.9))
    dp.add_handler(RegexProbabilityHandler(ur'(?iu)(.{0,6}|добр{0,6})\s?(прив|утр[оа]).{0,20}', callbacks.morning, 0.9))
    dp.add_handler(RegexProbabilityHandler(ur'(?iu)(.{0,10}|добр{0,10})\s?ночи.{0,20}', callbacks.night, 0.9))
    dp.add_handler(RegexProbabilityHandler(ur'(?iu).*(трахать|ебать|секс).*', callbacks.sex, 0.9))
    dp.add_handler(RegexProbabilityHandler(ur'(?iu).*(%s).*' % eat_choice,
                                           callbacks.eat, 0.9))
    dp.add_handler(RegexHandler(
        ur'(?iu).*глория,? покажи (?P<video_type>видос|видео|ролик) про ?(?P<keyword>.*)',
        callbacks.search_video_about, pass_groupdict=True))
    dp.add_handler(RegexHandler(
        ur'(?iu).*глория,? покажи (?P<video_type>видос|видео|ролик) ?"?(?P<keyword>.*)"?',
        callbacks.search_video, pass_groupdict=True))
    dp.add_handler(RegexHandler(
        ur'(?iu).*глория,? покажи како[йе]-?нибудь( другой)? (?P<video_type>видос|видео|ролик) про ?(?P<keyword>.*)',
        callbacks.search_some_video_about, pass_groupdict=True))
    dp.add_handler(RegexHandler(
        ur'(?iu).*глория,? покажи како[йе]-нибудь( другой)? (?P<video_type>видос|видео|ролик) ?"?(?P<keyword>.*)"?',
        callbacks.search_some_video, pass_groupdict=True))
    # log all errors
    dp.add_error_handler(callbacks.error)
    logger.debug(u"Handlers size: %s" % len(dp.handlers[0]))
