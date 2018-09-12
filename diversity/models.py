from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Manu Munoz-Herrera'

doc = """
Diversity game
"""


class Constants(BaseConstants):
    name_in_url = 'diversity'
    players_per_group = 4
    num_rounds = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    first = models.PositiveIntegerField(
        choices=[
            [0, 'orange'],
            [1, 'green'],
            [2, 'blue'],
            [3, 'red']
        ],
        widget=widgets.RadioSelect
    )
    second = models.PositiveIntegerField(
        choices=[
            [0, 'orange'],
            [1, 'green'],
            [2, 'blue'],
            [3, 'red']
        ],
        widget=widgets.RadioSelect
    )
    action = models.PositiveIntegerField(
        choices=[
            [0, 'orange'],
            [1, 'green'],
            [2, 'blue'],
            [3, 'red']
        ],
        widget=widgets.RadioSelect
    )

    def role(self):
        if self.id_in_group == 1:
            return 'A'
        if self.id_in_group == 2:
            return 'B'
        if self.id_in_group == 3:
            return 'C'
        if self.id_in_group == 4:
            return 'D'
