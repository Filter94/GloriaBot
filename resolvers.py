# coding=utf-8
import random
import re

SECOND_STAGE = 'second_stage'
ZAEBAL = 7
TIMES_WROTE = 'times_wrote'
LAST_USER_ID = 'last_user_id'
last_10_by_chats = {}


def true_with_probability(probability):
    return random.random() < probability


def resolve_regex_with_probability(regex, probability, message):
    if re.match(regex, message) is not None:
        return true_with_probability(probability)
    else:
        return False


def zaebal_resolver(message):
    if re.match(ur'.*', message.text) is not None:
        chat_id = message.chat.id
        user_id = message.from_user.id
        chat_last_msgs_by_user = last_10_by_chats.get(chat_id, {LAST_USER_ID: None, TIMES_WROTE: None})
        if chat_last_msgs_by_user[LAST_USER_ID] != user_id:
            chat_last_msgs_by_user[LAST_USER_ID] = user_id
            chat_last_msgs_by_user[TIMES_WROTE] = 1
            last_10_by_chats[chat_id] = chat_last_msgs_by_user
        else:
            chat_last_msgs_by_user[TIMES_WROTE] += 1
        if chat_last_msgs_by_user[TIMES_WROTE] >= ZAEBAL:
            chat_last_msgs_by_user[TIMES_WROTE] = 3
            return true_with_probability(0.9)
    else:
        return False


def kalinin_resolver(message):
    return resolve_regex_with_probability(ur'(?iu).*калинин.*', 0.5, message.text)


def net_resolver(message):
    return resolve_regex_with_probability(ur'(?iu).*нет[!?.)(]*$', 0.7, message.text)


def albert_resolver(message):
    return resolve_regex_with_probability(ur'(?iu).*альберт.*', 0.5, message.text)


def tema_resolver(message):
    return resolve_regex_with_probability(ur'(?iu).*(тема|тёма|артем).*', 0.5, message.text)


def geva_resolver(message):
    return resolve_regex_with_probability(ur'(?iu).*(гева|геворг|геворк).*', 0.5, message.text)


def stas_resolver(message):
    return resolve_regex_with_probability(ur'(?iu).*(стас|пидорас|пидор).*', 0.5, message.text)


def debug_resolver(message):
    return resolve_regex_with_probability(ur'debug', 1, message.text)


def ban_resolver(message):
    return resolve_regex_with_probability(ur'(?iu).*(на ?хуй|в пизду|впизду),? глория.*', 0.9, message.text)


def morning_resolver(message):
    return resolve_regex_with_probability(ur'(?iu)(.{0,6}прив.{0,20})|(.{0,3}утро.{0,20})', 0.9, message.text)


def night_resolver(message):
    return resolve_regex_with_probability(ur'(?iu)(.{0,6}ночи.{0,20}))', 0.9, message.text)


