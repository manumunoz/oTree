from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'min_effort'
    players_per_group = 4
    num_rounds = 10
    gain = 20
    cost = 10
    fix = 60
    # names = ['A','B','C','D',]
    # highpay = c(3)
    # lowpay = c(1)
    # nopay = c(0)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    min_effort = models.IntegerField()
    old_min_effort = models.IntegerField()

    def set_effort(self):
        for player in self.get_players():
            player.effort_a = self.get_player_by_role('1').effort
            player.effort_b = self.get_player_by_role('2').effort
            player.effort_c = self.get_player_by_role('3').effort
            player.effort_d = self.get_player_by_role('4').effort

        # for player in [a, b, c, d]:
        #     if self.coordination == 1 and player.action == player.favorite:
        #         player.is_winner = True
        #     else:
        #         player.is_winner = False
        #
        # for player in [a, b, c, d]:
        #     if self.coordination == 1:
        #         if player.is_winner is True:
        #             player.points = Constants.highpay
        #         else:
        #             player.points = Constants.lowpay
        #     else:
        #         player.points = Constants.nopay
        #
        # for player in [a, b, c, d]:
        #     player.total_points = sum([player.points for player in player.in_all_rounds()])


    def set_min_effort(self):
        players = self.get_players()
        efforts = sorted([p.effort for p in players])
        self.min_effort = efforts[0]

    def round_gains(self):
        for player in self.get_players():
            player.round_gains = (Constants.gain * self.min_effort) - (Constants.cost * player.effort) + Constants.fix




class Player(BasePlayer):
    effort_a = models.IntegerField()
    effort_b = models.IntegerField()
    effort_c = models.IntegerField()
    effort_d = models.IntegerField()
    old_effort_a = models.IntegerField()
    old_effort_b = models.IntegerField()
    old_effort_c = models.IntegerField()
    old_effort_d = models.IntegerField()

    effort = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'A'],
            [6, 'B'],
            [7, 'C']
        ]
    )

    old_effort = models.IntegerField()
    round_gains = models.IntegerField()
    old_round_gains = models.IntegerField()

    def role(self):
        return {1: '1', 2: '2', 3: '3', 4: '4'}[self.id_in_group]