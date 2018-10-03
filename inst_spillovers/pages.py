from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Start(Page):
    pass


class WaitPage1(WaitPage):
    pass

class Inst_1(Page):
    pass


class WaitPage2(WaitPage):
    pass

class Inst_2(Page):
    pass


class WaitPage3(WaitPage):
    pass

class Inst_3(Page):
    pass


page_sequence = [
    Start,
    WaitPage1,
    Inst_1,
    WaitPage2,
    Inst_2,
    WaitPage3,
    Inst_3,
]
