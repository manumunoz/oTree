from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class StartInst(Page):
    pass

class WelcomeInst(Page):
    pass


class PartOneInst(Page):
    form_model = 'player'
    form_fields = ['q1_symbol','q2_label']

    def q1_symbol_error_message(self, value):
        if value != 1:
            return 'In Part 1 your symbols are fixed for all 10 rounds'

    def q2_label_error_message(self, value):
        if value != 2:
            return 'In Part 1 your label is randomly assigned in each round'


class LinkingInst(Page):
    form_model = 'player'
    form_fields = ['q3_cost','q4_active']

    def q3_cost_error_message(self, value):
        if value != 1:
            return 'You will pay a cost when you propose a connection to another participant, no matter what the he/she does'

    def q4_active_error_message(self, value):
        if value != 3:
            return 'Active connections require being proposed by both participants'


class ActionInst(Page):
    form_model = 'player'
    form_fields = ['q5_count','q6_pay']

    def q5_count_error_message(self, value):
        if value != 3:
            return 'Active connections require being proposed by both participants'

    def q6_pay_error_message(self, value):
        if value != 2:
            return 'The cost is paid only for the connections proposed to others'


class ResultsInst(Page):
    form_model = 'player'
    form_fields = ['q7_points','q8_payoffs']

    def q7_points_error_message(self, value):
        if value != 1:
            return 'In Part 1 your symbols are fixed for all 10 rounds'

    def q8_payoffs_error_message(self, value):
        if value != 1:
            return 'In Part 1 your symbols are fixed for all 10 rounds'


class SummaryInst(Page):
    pass

# You will observe your type, choose connection, observe the network, choose an action, and observe your earnings.


page_sequence = [
    StartInst,
    WelcomeInst,
    PartOneInst,
    LinkingInst,
    ActionInst,
    ResultsInst,
    SummaryInst,
]
