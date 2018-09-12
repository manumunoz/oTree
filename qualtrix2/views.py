from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Part2a(Page):
    pass

class Part2b(Page):
    pass

class Part2c(Page):
    pass

class Hiring(Page):
    form_model = models.Player
    form_fields = ['hiring_decision']

class Results(Page):
    pass

#    Your ID is {{ participant.code }}

page_sequence = [
    Part2a,
    Part2b,
    Part2c,
    Hiring,
    Results,
]
