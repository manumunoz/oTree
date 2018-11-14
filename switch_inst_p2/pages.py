from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Type(Page):
    def is_displayed(self):
        return self.round_number == 1

class WelcomeP2(Page):
    pass


class GroupChangeInst(Page):
    form_model = 'player'
    form_fields = ['new_symbol']

    def new_symbol_error_message(self, value):
        if value != 3:
            return 'In Part 2 you can change your group (and appearance) in each round'


page_sequence = [
    Type,
    WelcomeP2,
    GroupChangeInst,
]
