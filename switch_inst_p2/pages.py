from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class GroupChangeInst(Page):
    form_model = 'player'
    form_fields = ['new_symbol']

    def new_symbol_error_message(self, value):
        if value != 3:
            return 'In Part 2 you can change your group (and appearance) in each round'

class SummaryInst(Page):
    pass

# You will observe your type, choose connection, observe the network, choose an action, and observe your earnings.


page_sequence = [
    GroupChangeInst,
    # SummaryInst,
]
