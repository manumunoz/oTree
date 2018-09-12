from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Language(Page):

    form_model = models.Player
    form_fields = ['language']

class Quest1ES(Page):

    def is_displayed(self):
        return self.player.language == 1 # Spanish

    form_model = models.Player
    form_fields = ['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12']

class Quest2ES(Page):

    def is_displayed(self):
        return self.player.language == 1 # Spanish

    form_model = models.Player
    form_fields = ['q13','q14','q15','q16','q17','q18','q19','q20','q21','q22','q23','q24']


class Quest3ES(Page):

    def is_displayed(self):
        return self.player.language == 1 # Spanish

    form_model = models.Player
    form_fields = ['q25','q26','q27','q28','q29','q30','q31','q32','q33','q34','q35','q36']

class Quest1EN(Page):

    def is_displayed(self):
        return self.player.language == 2 # English

    form_model = models.Player
    form_fields = ['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12']

class Quest2EN(Page):

    def is_displayed(self):
        return self.player.language == 2 # English

    form_model = models.Player
    form_fields = ['q13','q14','q15','q16','q17','q18','q19','q20','q21','q22','q23','q24']


class Quest3EN(Page):

    def is_displayed(self):
        return self.player.language == 2 # English

    form_model = models.Player
    form_fields = ['q25','q26','q27','q28','q29','q30','q31','q32','q33','q34','q35','q36']



page_sequence = [
    Language,
    Quest1ES,
    Quest2ES,
    Quest3ES,
    Quest1EN,
    Quest2EN,
    Quest3EN,
]
