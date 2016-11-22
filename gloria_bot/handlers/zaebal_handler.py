#!/usr/bin/env python
""" This module contains the ZaebalHandler class """
from gloria_bot.handlers.handlers_helpers import true_with_probability
from gloria_bot.handlers.regex_probability_handler import RegexProbabilityHandler


class ZaebalHandler(RegexProbabilityHandler):
    """
    This handler determines if the person zaebal you enough.
    """
    ZAEBAL = 7
    COOLDOWN_COUNT = 3
    DEFAULT_PROBABILITY = 1
    _TIMES_WROTE = 'times_wrote'
    _LAST_USER_ID = 'last_user_id'
    _last_10_by_chats = {}

    def __init__(self,
                 pattern,
                 callback,
                 probability=DEFAULT_PROBABILITY,
                 cooldown_count=COOLDOWN_COUNT,
                 zaebal_count=ZAEBAL,
                 pass_groups=False,
                 pass_groupdict=False,
                 pass_update_queue=False,
                 pass_job_queue=False,
                 pass_user_data=False,
                 pass_chat_data=False):
        super(ZaebalHandler, self).__init__(
            pattern,
            callback,
            pass_groups=pass_groups,
            pass_groupdict=pass_groupdict,
            pass_update_queue=pass_update_queue,
            pass_job_queue=pass_job_queue,
            pass_user_data=pass_user_data,
            pass_chat_data=pass_chat_data)
        self.pass_groupdict = pass_groupdict
        self.zaebal_count = zaebal_count
        self.probability = probability
        self.cooldown_count = cooldown_count

    def check_update(self, update):
        if super(ZaebalHandler, self).check_update(update):
            chat_id = update.message.chat_id
            user_id = update.message.from_user.id
            chat_last_msgs_by_user = self._last_10_by_chats.get(chat_id, {
                self._LAST_USER_ID: None, self._TIMES_WROTE: None,
            })
            if chat_last_msgs_by_user[self._LAST_USER_ID] != user_id:
                chat_last_msgs_by_user[self._LAST_USER_ID] = user_id
                chat_last_msgs_by_user[self._TIMES_WROTE] = 1
                self._last_10_by_chats[chat_id] = chat_last_msgs_by_user
            else:
                chat_last_msgs_by_user[self._TIMES_WROTE] += 1
            if chat_last_msgs_by_user[self._TIMES_WROTE] >= self.zaebal_count:
                chat_last_msgs_by_user[self._TIMES_WROTE] = self.cooldown_count
                return true_with_probability(self.probability)
            else:
                return False
        else:
            return False
