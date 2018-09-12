from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Manu'

doc = """
Shows the total payoffs for a real effort task and the unique identification number for the participant 
"""


class Constants(BaseConstants):
    name_in_url = 'final'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
