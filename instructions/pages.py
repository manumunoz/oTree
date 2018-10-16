from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomeInst(Page):
    pass

class DecisionsInst(Page):
    form_model = 'player'
    form_fields = ['q1_symbol','q2_label', 'q4_active', 'q5_count']

    def q1_symbol_error_message(self, value):
        if value != 1:
            return 'In Part 1 your group and appearance are fixed for all 10 rounds'

    def q2_label_error_message(self, value):
        if value != 2:
            return 'In Part 1 your label is randomly assigned in each round'

    def q4_active_error_message(self, value):
        if value != 3:
            return 'Active relations require being proposed by both participants'

    def q5_count_error_message(self, value):
        if value != 3:
            return 'Active relations require being proposed by both participants'

class PointsInst(Page):
    pass

class SummaryInst(Page):
    pass

# You will observe your type, choose connection, observe the network, choose an action, and observe your earnings.


page_sequence = [
    # StartInst,
    WelcomeInst,
    DecisionsInst,
    PointsInst,
    # PartOneInst,
    # LinkingInst,
    # ActionInst,
    # ResultsInst,
    # SummaryInst,
]
