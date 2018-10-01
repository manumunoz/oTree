from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):

    def play_round(self):

        yield (pages.FirstSignal, {'first': random.randint(1, 4)})

        yield (pages.SecondSignal, {'second': random.randint(1, 4)})

        yield (pages.Action, {'action': random.randint(1, 4)})

        yield (pages.Results)



# otree test p1_no2 --export=test_p1_no2