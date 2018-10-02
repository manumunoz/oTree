from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Start(Page):
    pass


class Inst_1(Page):
    pass


page_sequence = [
    Start,
    Inst_1
]
