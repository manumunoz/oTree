from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'network_study'
    players_per_group = 4
    num_rounds = 2
    names = ['A','B','C','D',]
    highpay = c(3)
    lowpay = c(1)
    nopay = c(0)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    coordination = models.BooleanField(initial=False)

    def set_coordination(self):
        print('in set_payoffs')
        a = self.get_player_by_role('A')
        b = self.get_player_by_role('B')
        c = self.get_player_by_role('C')
        d = self.get_player_by_role('D')

        if a.act == b.act == c.act == d.act:
            self.coordination = 1

        for player in [a, b, c, d]:
            if self.coordination == 1 and player.act == player.id_in_group:
                player.is_winner = True
            else:
                player.is_winner = False

        for player in [a, b, c, d]:
            if self.coordination == 1:
                if player.is_winner is True:
                    player.payoff = Constants.highpay
                else:
                    player.payoff = Constants.lowpay
            else:
                player.payoff = Constants.nopay

class Player(BasePlayer):
    msg1 = models.IntegerField(widget=widgets.RadioSelect,
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D']
        ]
    )
    msg2 = models.IntegerField(widget=widgets.RadioSelect,
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D']
        ]
    )
    act = models.IntegerField(widget=widgets.RadioSelect,
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D']
        ]
    )

    is_winner = models.BooleanField()

    def role(self):
        if self.id_in_group == 1:
            return 'A'
        if self.id_in_group == 2:
            return 'B'
        if self.id_in_group == 3:
            return 'C'
        if self.id_in_group == 4:
            return 'D'
