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
    min_pay = 10000
    names = 11

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    test1=models.IntegerField()

    participants = models.PositiveIntegerField(
        choices=[
            [1, 'Only myself'],
            [2, '11 including myself'],
            [3, '6 including myself']
        ],
        widget=widgets.RadioSelect
    )

    change = models.PositiveIntegerField(
        choices=[
            [1, 'They are fixed and do not change'],
            [2, 'The computer changes them in every round'],
            [3, 'I can change them in every round'],
        ],
        widget=widgets.RadioSelect
    )

    phases = models.PositiveIntegerField(
        choices=[
            [1, '1 Phase'],
            [2, '2 Phases'],
            [3, '3 Phases']
        ],
        widget=widgets.RadioSelect
    )
