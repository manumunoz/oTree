from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class First(Page):
    form_model = 'player'
    form_fields = ['first']

class FirstWaitPage(WaitPage):
    pass

class Second(Page):
    form_model = 'player'
    form_fields = ['second']

class SecondWaitPage(WaitPage):
    pass

class Action(Page):
    form_model = 'player'
    form_fields = ['action']

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass

class Results(Page):
    pass


page_sequence = [
    First,
    # FirstWaitPage,
    # Second,
    # SecondWaitPage,
    # Action,
    # ResultsWaitPage,
    # Results
]
