from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
from collections import OrderedDict
import json


class BeforeEffortWP(WaitPage):
    def after_all_players_arrive(self):
        if self.round_number > 1:
            self.group.old_min_effort = self.group.in_round(self.round_number - 1).min_effort
        else:
            self.group.old_min_effort = 0

        for player in self.group.get_players():
            if self.round_number > 1:
                player.old_effort= player.in_round(self.round_number - 1).effort
                player.old_effort_a = player.in_round(self.round_number - 1).effort_a
                player.old_effort_b = player.in_round(self.round_number - 1).effort_b
                player.old_effort_c = player.in_round(self.round_number - 1).effort_c
                player.old_effort_d = player.in_round(self.round_number - 1).effort_d
                player.old_round_gains = player.in_round(self.round_number - 1).round_gains
            else:
                player.old_effort = 0
                player.old_effort_b = 0
                player.old_effort_a = 0
                player.old_effort_c = 0
                player.old_effort_d = 0
                player.old_round_gains = 0


class Effort(Page):
    form_model = 'player'
    form_fields = ['effort']


class BeforeNextRoundWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_effort()
        self.group.set_min_effort()
        self.group.round_gains()

class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    BeforeEffortWP,
    Effort,
    BeforeNextRoundWP,
    Results
]
