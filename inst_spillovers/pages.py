from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Start(Page):
    pass


class Inst1_WP(WaitPage):
    def after_all_players_arrive(self):
        pass

class Inst_1(Page):
    pass


class Inst2_WP(WaitPage):
    def after_all_players_arrive(self):
        pass

class Inst_2(Page):
    pass


class Inst3_WP(WaitPage):
    def after_all_players_arrive(self):
        pass

class Inst_3(Page):
    pass


page_sequence = [
    Start,
    Inst_1,
    Inst_2,
    Inst_3,
]
