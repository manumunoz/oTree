from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1
    min_pay = 5
    names = 7
    others = names - 1
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    exchange = 2
    instructions_template= 'instructions/Instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    q1_symbol = models.PositiveIntegerField(
        choices=[
            [1, 'They are fixed and do not change'],
            [2, 'The computer changes them in every round'],
            [3, 'I can change them in every round'],
        ],
        widget=widgets.RadioSelect
    )

    q2_label = models.PositiveIntegerField(
        choices=[
            [1, 'It is fixed and does not change'],
            [2, 'The computer changes it in every round'],
            [3, 'I can change it in every round'],
        ],
        widget=widgets.RadioSelect
    )

    q3_cost = models.PositiveIntegerField(
        choices=[
            [1, 'When I propose a connection to another participant regardless of he/she proposing a connection to me'],
            [2, 'When another participant proposes a connection to me regardless of me proposing a connection to him/her'],
            [3, 'When I propose a connection to a participant who also proposes a connection to me']
        ],
        widget=widgets.RadioSelect
    )

    q4_active = models.PositiveIntegerField(
        choices=[
            [1, 'When I propose a connection to another participant regardless of he/she proposing a connection to me'],
            [2, 'When another participant proposes a connection to me regardless of me proposing a connection to him/her'],
            [3, 'When I propose a connection to a participant who also proposes a connection to me']
        ],
        widget=widgets.RadioSelect
    )

    q5_count = models.PositiveIntegerField(
        choices=[
            [1, '5'],
            [2, '4'],
            [3, '3']
        ],
        widget=widgets.RadioSelect
    )

    q6_pay = models.PositiveIntegerField(
        choices=[
            [1, '3 active connections with others x 2 points = 6 points'],
            [2, '4 proposed connection to others  x 2 points = 8 points'],
            [3, '4 proposed connection from others  x 2 points = 8 points']
        ],
        widget=widgets.RadioSelect
    )

    q7_points = models.PositiveIntegerField(
        choices=[
            [1, 'When I propose a connection to another participant'],
            [2, 'When another participant proposes a connection to me'],
            [3, 'When I propose a connection to a participant who also proposes a connection to me']
        ],
        widget=widgets.RadioSelect
    )

    q8_payoffs = models.PositiveIntegerField(
        choices=[
            [1, 'When I propose a connection to another participant'],
            [2, 'When another participant proposes a connection to me'],
            [3, 'When I propose a connection to a participant who also proposes a connection to me']
        ],
        widget=widgets.RadioSelect
    )