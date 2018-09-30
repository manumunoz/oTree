from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from collections import OrderedDict
import json

author = 'Manu Munoz'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'group_spillover'
    names = ['1', '2', '3', '4']
    players_per_group = len(names)
    num_rounds = 2


class Subsession(BaseSubsession):
    def creating_session(self):
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
    total_coordination = models.IntegerField(initial=0)
    old_coordination = models.IntegerField()
    network_data = models.LongStringField()
    win = models.IntegerField(initial=0)
    old_win = models.IntegerField()
    win_one = models.IntegerField(initial=0)
    win_two = models.IntegerField(initial=0)
    win_three = models.IntegerField(initial=0)
    win_four = models.IntegerField(initial=0)
    goal_achieved = models.IntegerField(initial=0)

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

    def total_values(self):
        self.total_coordination = sum([self.in_all_rounds().coordination])

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
    given_type = models.IntegerField() # combination of symbol and preference
    liked_action = models.IntegerField()
    old_action = models.PositiveIntegerField()
    action_one = models.IntegerField(initial=0)
    action_two = models.IntegerField(initial=0)
    action_three = models.IntegerField(initial=0)
    action_four = models.IntegerField(initial=0)

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
            self.action_two = 0
            self.action_three = 0
            self.action_four = 0
        elif self.action == 2:
            self.action_one = 0
            self.action_two = 1
            self.action_three = 0
            self.action_four = 0
        elif self.action == 3:
            self.action_one = 0
            self.action_two = 0
            self.action_three = 1
            self.action_four = 0
        else:
            self.action_one = 0
            self.action_two = 0
            self.action_three = 0
            self.action_four = 1

    def get_old_action(self):
        self.old_action = self.in_round(self.round_number - 1).action
        #
        # if self.subsession.round_number > 1:
        #     self.old_action = self.player.in_round(self.round_number - 1).action
        # else:
        #     self.old_action = 0

    name = models.StringField()
    friends = models.LongStringField()

# for i in Constants.names:
#     Player.add_to_class(i, models.BooleanField(widget=widgets.CheckboxInput, blank=True))