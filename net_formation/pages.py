from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    form_model = 'player'
    form_fields = ['network_data']

class Results(Page):
    pass


page_sequence = [
    Introduction,
    Results,
]
