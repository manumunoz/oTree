from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import itertools


author = 'Manu Munoz'

doc = """
inst_spillovers
"""


class Constants(BaseConstants):
    name_in_url = 'inst_spillovers'
    names = ['1', '2', '3', '4']
    players_per_group = len(names)
    num_rounds = 1
    show_up = 5
    total_group_pay = 40 # Value in dollars for total group earnings
    total_group_no_pay = 0
    goal_value = 12 # Number of coordinations needed to achieve the goal
    no_goal_value = 11
    total_number_rounds = 20

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


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treat = models.IntegerField() # Treatments from 1 to 3
