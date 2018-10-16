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
            [2, 'The computer changes them in each round'],
            [3, 'I can change them in each round'],
        ],
        widget=widgets.RadioSelect
    )

    q2_label = models.PositiveIntegerField(
        choices=[
            [1, 'It is fixed and does not change'],
            [2, 'The computer changes it in each round'],
            [3, 'I can change it in each round'],
        ],
        widget=widgets.RadioSelect
    )

    q3_cost = models.PositiveIntegerField(
        choices=[
            [1, 'When I propose a relation to another player regardless of he/she proposing a relation to me'],
            [2, 'When another player proposes a relation to me regardless of me proposing a relation to him/her'],
            [3, 'When I propose a relation to a player who also proposes a relation to me']
        ],
        widget=widgets.RadioSelect
    )

    q4_active = models.PositiveIntegerField(
        choices=[
            [1, 'When I propose a relation to another player regardless of he/she proposing a relation to me'],
            [2, 'When another player proposes a relation to me regardless of me proposing a relation to him/her'],
            [3, 'When I propose a relation to a player who also proposes a relation to me']
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
            [1, '3 active relation with others x 2 points = 6 points'],
            [2, '4 proposed relation to others  x 2 points = 8 points'],
            [3, '4 proposed relation from others  x 2 points = 8 points']
        ],
        widget=widgets.RadioSelect
    )

    q7_points = models.PositiveIntegerField(
        choices=[
            [1, 'a'],
            [2, 'b'],
            [3, 'c']
        ],
        widget=widgets.RadioSelect
    )

    q8_payoffs = models.PositiveIntegerField(
        choices=[
            [1, 'x'],
            [2, 'y'],
            [3, 'z']
        ],
        widget=widgets.RadioSelect
    )