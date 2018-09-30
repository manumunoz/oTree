from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
from collections import OrderedDict
import json


class BeforeSignalWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.displaying_network()

    # def vars_for_template(self):
    #     self.player.vars_from_previous_round()


class FirstSignal(Page):
    form_model = 'player'
    form_fields = ['first']


class BeforeSecondSignalWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.displaying_network()


class SecondSignal(Page):
    form_model = 'player'
    form_fields = ['second']


class BeforeActionlWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.displaying_network()


class Action(Page):
    form_model = 'player'
    form_fields = ['action']

    def before_next_page(self):
        self.player.choice_value()


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        players = group.get_players()
        ones = [p.action_one for p in players]
        group.total_one = sum(ones)
        twos = [p.action_two for p in players]
        group.total_two = sum(twos)
        threes = [p.action_three for p in players]
        group.total_three = sum(threes)
        fours = [p.action_four for p in players]
        group.total_four = sum(fours)

        self.group.determine_win()

        # cumulative_payoff = sum([p.payoff for p in self.player.in_all_rounds()])
        # Esta es para coordinación total y para coordinación por acción across periods

class Results(Page):
    def is_displayed(self):
        return self.round_number == 10


page_sequence = [
    BeforeSignalWP,
    FirstSignal,
    BeforeSecondSignalWP,
    SecondSignal,
    BeforeActionlWP,
    Action,
    ResultsWaitPage,
    Results
]
