from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'canvas'
    players_per_group = 4
    num_rounds = 1


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
        return {1: 'P1', 2: 'P2', 3: 'P3', 4: 'P4'}[self.id_in_group]

