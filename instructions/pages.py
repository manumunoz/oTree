from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomeInst(Page):
    pass

class PartOneInst(Page):
    form_model = 'player'
    form_fields = ['change']

    def change_error_message(self, value):
        # print('value is', value)
        if value != 1:
            return 'In Part 1 your symbols are fixed for all 10 rounds'


class LinkingInst(Page):
    form_model = 'player'
    form_fields = ['change']

    def change_error_message(self, value):
        print('value is', value)
        if value != 1:
            return 'In Part 1 your symbols are fixed for all 10 rounds'
# proposals: directed but only count if reciprocal

class ActionInst(Page):
    form_model = 'player'
    form_fields = ['change']

    def change_error_message(self, value):
        print('value is', value)
        if value != 1:
            return 'In Part 1 your symbols are fixed for all 10 rounds'

# action: two options and you earn points depending on your choice and the choice of your connections.
# You are not affected by someone else's choice of she is not a connection

class ResultsInst(Page):
    form_model = 'player'
    form_fields = ['change']

    def change_error_message(self, value):
        print('value is', value)
        if value != 1:
            return 'In Part 1 your symbols are fixed for all 10 rounds'

# You get points of you choose the same as your connections (coordinate) and you loose points if you loose points if
# you miscoordinate. Circles earn 4 or 2, etc

class ExamplesInst(Page):
    pass

# Case 1:
# Case 2:

class SummaryInst(Page):
    pass

# You will observe your type, choose connection, observe the network, choose an action, and observe your earnings.


page_sequence = [
    WelcomeInst,
    PartOneInst,
    LinkingInst,
    ActionInst,
    ResultsInst,
]
