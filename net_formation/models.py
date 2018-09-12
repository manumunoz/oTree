from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'net_formation'
    players_per_group = None
    num_rounds = 1
    names = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10',]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    network_data = models.StringField()
