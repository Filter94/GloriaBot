#!/usr/bin/env python
""" This module contains the RegexProbabilityHandler class """
from telegram.ext import RegexHandler

from gloria_bot.handlers.handlers_helpers import true_with_probability


class RegexProbabilityHandler(RegexHandler):
    """
    This handlers is basically RegexHandler which handles the request with given probability
    """
    DEFAULT_PROBABILITY = 1

    def __init__(self,
                 pattern,
                 callback,
                 probability=DEFAULT_PROBABILITY,
                 pass_groups=False,
                 pass_groupdict=False,
                 pass_update_queue=False,
                 pass_job_queue=False,
                 pass_user_data=False,
                 pass_chat_data=False):
        super(RegexProbabilityHandler, self).__init__(
            pattern,
            callback,
            pass_groups=pass_groups,
            pass_groupdict=pass_groupdict,
            pass_update_queue=pass_update_queue,
            pass_job_queue=pass_job_queue,
            pass_user_data=pass_user_data,
            pass_chat_data=pass_chat_data)
        self.probability = probability

    def check_update(self, update):
        if super(RegexProbabilityHandler, self).check_update(update):
            return true_with_probability(self.probability)
        else:
            return False
