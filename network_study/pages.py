from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
from collections import OrderedDict
import json

class Msg1(Page):
    form_model = 'player'
    form_fields = ['msg1']

class Msg2(Page):
    form_model = 'player'
    form_fields = ['msg2']

class Action(Page):
    form_model = 'player'
    form_fields = ['act']

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_coordination()

class Results(Page):
    pass


page_sequence = [
    Msg1,
    Msg2,
    Action,
    ResultsWaitPage,
    Results
]
