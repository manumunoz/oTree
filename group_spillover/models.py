from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from collections import OrderedDict
import json
import itertools


author = 'Manu Munoz'

doc = """
Group Spillovers
"""


class Constants(BaseConstants):
    name_in_url = 'group_spillover'
    names = ['1', '2', '3', '4']
    players_per_group = len(names)
    num_rounds = 20
    total_number_rounds = 2
    highpay = 3
    lowpay = 1
    nopay = 0
    show_up = 5
    total_group_pay = 40 # Value in dollars for total group earnings
    total_group_no_pay = 0
    goal_value = 12 # Number of coordinations needed to achieve the goal
    # instructions_template = 'group_spillover/Instructions.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        treat = itertools.cycle([1, 2, 3])
        # for p in self.get_players():
        #     p.treat = next(treat)
        for p in self.get_players():
            if 'treatment' in self.session.config:
                # demo mode
                p.treat = self.session.config['treatment']
            else:
                # live experiment mode
                p.treat = next(treat)

            if p.treat == 1:
                p.favorite = 1
            elif p.treat == 2:
                if p.id_in_group == 1 or p.id_in_group == 2:
                    p.favorite = 1
                else:
                    p.favorite = 4
            else:
                if p.id_in_group == 1:
                    p.favorite = 1
                elif p.id_in_group == 2:
                    p.favorite = 2
                elif p.id_in_group == 3:
                    p.favorite = 3
                else:
                    p.favorite = 4

        num_players_err = 'Too many participants for such a short name list'
        # the following may create issues with mTurk sessions where num participants is doubled
        assert len(Constants.names) <= self.session.num_participants, num_players_err
        for g in self.get_groups():
            cur_names = Constants.names.copy()
            # random.shuffle(cur_names)
            for i, p in enumerate(g.get_players()):
                p.name = cur_names[i]


class Group(BaseGroup):
    total_one = models.IntegerField()
    total_two = models.IntegerField()
    total_three = models.IntegerField()
    total_four = models.IntegerField()
    coordination = models.IntegerField(initial=0)
    old_coordination = models.IntegerField(initial=0)
    total_coordination = models.IntegerField(initial=0)
    old_total_coordination = models.IntegerField(initial=0)
    network_data = models.LongStringField()
    win = models.IntegerField(initial=0)
    old_win = models.IntegerField()
    win_one = models.IntegerField(initial=0)
    win_two = models.IntegerField(initial=0)
    win_three = models.IntegerField(initial=0)
    win_four = models.IntegerField(initial=0)
    goal_achieved = models.IntegerField(initial=0)
    group_points = models.IntegerField(initial=0)
    group_total_points = models.IntegerField(initial=0)
    old_group_total_points = models.IntegerField(initial=0)
    total_win_one = models.IntegerField(initial=0)
    total_win_two = models.IntegerField(initial=0)
    total_win_three = models.IntegerField(initial=0)
    total_win_four = models.IntegerField(initial=0)
    old_total_win_one = models.IntegerField(initial=0)
    old_total_win_two = models.IntegerField(initial=0)
    old_total_win_three = models.IntegerField(initial=0)
    old_total_win_four = models.IntegerField(initial=0)

    def determine_win(self):
        if self.total_one == 4:
            self.win = 1
        elif self.total_two == 4:
            self.win = 2
        elif self.total_three == 4:
            self.win = 3
        elif self.total_four == 4:
            self.win = 4
        if self.win == 1:
            self.win_one = 1
        elif self.win == 2:
            self.win_two = 1
        elif self.win == 3:
            self.win_three = 1
        elif self.win == 4:
            self.win_four = 1
        if self.win != 0:
            self.coordination = 1

    def set_coordination(self):
        a = self.get_player_by_role('1')
        b = self.get_player_by_role('2')
        c = self.get_player_by_role('3')
        d = self.get_player_by_role('4')

        for player in [a, b, c, d]:
            if self.coordination == 1 and player.action == player.favorite:
                player.is_winner = True
            else:
                player.is_winner = False

        for player in [a, b, c, d]:
            if self.coordination == 1:
                if player.is_winner is True:
                    player.points = Constants.highpay
                else:
                    player.points = Constants.lowpay
            else:
                player.points = Constants.nopay

        for player in [a, b, c, d]:
            player.total_points = sum([player.points for player in player.in_all_rounds()])

    def total_values(self):
        self.total_coordination = sum([g.coordination for g in self.in_all_rounds()])
        if self.total_coordination >= Constants.goal_value:
            self.goal_achieved = 1
        else:
            self.goal_achieved = 0
        self.group_total_points = sum([g.group_points for g in self.in_all_rounds()])
        self.total_win_one = sum([g.win_one for g in self.in_all_rounds()])
        self.total_win_two = sum([g.win_two for g in self.in_all_rounds()])
        self.total_win_three = sum([g.win_three for g in self.in_all_rounds()])
        self.total_win_four = sum([g.win_four for g in self.in_all_rounds()])

    def total_points(self):
        players = self.get_players()
        point = [p.points for p in players]
        self.group_points = sum(point)

    def finalpay_value(self):
        for player in self.get_players():
            if self.round_number == Constants.num_rounds and self.goal_achieved == 1:
                player.final_pay = (player.total_points * Constants.total_group_pay)/self.group_total_points
            else:
                player.final_pay = 0

    def payoff_value(self):
        for player in self.get_players():
            if self.round_number == Constants.num_rounds:
                player.payoff = player.final_pay
            else:
                player.payoff = 0

    def displaying_network(self):
        nodes = [{'data': {'id': i, 'name': i, 'first': self.get_player_by_id(i).first, 'second': self.get_player_by_id(i).second,
                           'action': self.get_player_by_id(i).action, 'old_action': self.get_player_by_id(i).old_action},  'group': 'nodes'} for i in Constants.names]
        edges = []
        elements = nodes + edges
        style = [{'selector': 'node', 'style': {'content': 'data(name)'}}]
        self.network_data = json.dumps({'elements': elements,
                                        'style': style,
                                        })


class Player(BasePlayer):
    treat = models.IntegerField() # Treatments from 1 to 3
    old_action = models.PositiveIntegerField()
    action_one = models.IntegerField(initial=0)
    action_two = models.IntegerField(initial=0)
    action_three = models.IntegerField(initial=0)
    action_four = models.IntegerField(initial=0)
    points = models.IntegerField()
    total_points = models.IntegerField(initial=0)
    old_total_points = models.IntegerField(initial=0)
    is_winner = models.BooleanField()
    favorite = models.IntegerField()
    final_pay = models.FloatField()

    first = models.PositiveIntegerField(
        choices=[
            [1, 'orange'],
            [2, 'green'],
            [3, 'blue'],
            [4, 'red']
        ],
        widget=widgets.RadioSelect
    )
    second = models.PositiveIntegerField(
        choices=[
            [1, 'orange'],
            [2, 'green'],
            [3, 'blue'],
            [4, 'red']
        ],
        widget=widgets.RadioSelect
    )
    action = models.PositiveIntegerField(
        choices=[
            [1, 'orange'],
            [2, 'green'],
            [3, 'blue'],
            [4, 'red']
        ],
        widget=widgets.RadioSelect
    )

    def role(self):
        return {1: '1', 2: '2', 3: '3', 4: '4'}[self.id_in_group]

    def choice_value(self):
        if self.action == 1:
            self.action_one = 1
        elif self.action == 2:
            self.action_two = 1
        elif self.action == 3:
            self.action_three = 1
        else:
            self.action_four = 1

    # def set_payoffs(self):
    #     if self.round_number == Constants.num_rounds:
    #         self.payoff = self.final_pay
    #     else:
    #         self.payoff = 0

    name = models.StringField()
    friends = models.LongStringField()

# for i in Constants.names:
#     Player.add_to_class(i, models.BooleanField(widget=widgets.CheckboxInput, blank=True))