from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        yield (pages.FirstSignal, {'first': random.randint(1, 4)})
        yield (pages.SecondSignal, {'second': random.randint(1, 4)})
        if self.round_number <= 4:
            yield (pages.Action, {'action': self.subsession.round_number})
        elif self.round_number <= 6:
            yield (pages.Action, {'action': 1})
        elif self.round_number <= 8:
            yield (pages.Action, {'action': 2})
        elif self.round_number <= 10:
            yield (pages.Action, {'action': 3})
        elif self.round_number <= 12:
            yield (pages.Action, {'action': 4})
        else:
            yield (pages.Action, {'action': random.randint(1, 4)})
        if self.round_number == Constants.num_rounds:
            yield (pages.Results)



    #otree test group_spillover_high --export=test_high