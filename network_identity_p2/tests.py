from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        if self.player.name == 1:
            yield (pages.Formation,
                   {'2': random.randint(0,1), '3': random.randint(0,1), '4': random.randint(0,1),
                    '5': random.randint(0,1), '6': random.randint(0,1), '7': random.randint(0,1)})
        elif self.player.name == 2:
            yield (pages.Formation,
                   {'1': random.randint(0,1), '3': random.randint(0,1), '4': random.randint(0,1),
                    '5': random.randint(0,1), '6': random.randint(0,1), '7': random.randint(0,1)})
        elif self.player.name == 3:
            yield (pages.Formation,
                   {'1': random.randint(0,1), '2': random.randint(0,1), '4': random.randint(0,1),
                    '5': random.randint(0,1), '6': random.randint(0,1), '7': random.randint(0,1)})
        elif self.player.name == 4:
            yield (pages.Formation,
                   {'1': random.randint(0,1), '2': random.randint(0,1), '3': random.randint(0,1),
                    '5': random.randint(0,1), '6': random.randint(0,1), '7': random.randint(0,1)})
        elif self.player.name == 5:
            yield (pages.Formation,
                   {'1': random.randint(0,1), '2': random.randint(0,1), '3': random.randint(0,1), '4': random.randint(0,1),
                    '6': random.randint(0,1), '7': random.randint(0,1)})
        elif self.player.name == 6:
            yield (pages.Formation,
                   {'1': random.randint(0,1), '2': random.randint(0,1), '3': random.randint(0,1), '4': random.randint(0,1),
                    '5': random.randint(0,1), '7': random.randint(0,1)})
        else:
            yield (pages.Formation,
                   {'1': random.randint(0,1), '2': random.randint(0,1), '3': random.randint(0,1), '4': random.randint(0,1),
                    '5': random.randint(0,1), '6': random.randint(0,1)})

        yield (pages.Action,
               {'action': random.randint(0,1)})

        yield (pages.Results)

# otree test network_identity --export=test_identity