from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
from collections import OrderedDict
import json


class BeforeChosenTypeWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.displaying_network()
        self.group.summing_initial_types()


class ChosenType(Page):
    form_model = 'player'
    form_fields = ['chosen_type']


class BeforeFormationWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.choosing_types()
        self.group.displaying_network()
        self.group.summing_types()


class Formation(Page):
    form_model = 'player'

    def get_form_fields(self):
        return [i.name for i in self.player.get_others_in_group()]

    def before_next_page(self):
        self.player.friends = json.dumps([i.name for i in self.player.get_others_in_group() if getattr(self.player, i.name)])


class BeforeActionWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.forming_network()
        self.group.calculate_props_from_and_links() # una vez generada la red, calculo las props from
        self.group.calculate_degree()
        self.group.linking_costs()


class Action(Page):
    form_model = 'player'
    form_fields = ['action']

    def vars_for_template(self):
        self.group.forming_network()

    # def before_next_page(self):
    #     self.player.calculate_degree()


class BeforeResultsWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.calculate_actions()
        self.group.sum_coordinations()
        self.group.coordination_score()
        self.group.values_coordination()
        self.group.round_gains()
        self.group.round_payoffs()
        self.group.forming_network()
        self.group.summing_choices()


class Results(Page):
    def vars_for_template(self):
        self.group.forming_network()



page_sequence = [
    # Welcome,
    BeforeChosenTypeWP,
    ChosenType,
    BeforeFormationWP,
    Formation,
    BeforeActionWP,
    Action,
    BeforeResultsWP,
    Results
]