from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Manu Munoz'

doc = """
inst_spillovers
"""


class Constants(BaseConstants):
    name_in_url = 'inst_spillovers'
    players_per_group = None
    num_rounds = 1
    show_up = 5



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
