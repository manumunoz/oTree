from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Demographics(Page):
    form_model = models.Player
    form_fields = ['age',
                   'gender']


class CognitiveReflectionTest(Page):
    form_model = models.Player
    form_fields = ['crt_bat',
                   'crt_widget',
                   'crt_lake']

class ChooseNames(Page):
    form_model = models.Player
    form_fields = ['names']

    def names_choices(self):
        if self.player.gender == 'Male':
            return Constants.male_names
        else:
            return Constants.female_names

class ShowMatrix(Page):
    form_model = models.Player
    form_fields = ['sumOfMax']

    def vars_for_template(self):
        return{
            'matrix_left': Constants.all_left_matrix[self.subsession.round_number-1],
            'matrix_right':Constants.all_right_matrix[self.subsession.round_number-1],
        }

class Result(Page):
    form_model = models.Player
    def vars_from_template(self):
        return{
            'max_left': Constants.max_left,
            'max_right': Constants.max_right,
        }
page_sequence = [
    ChooseNames,
    ShowMatrix,
    Result,
]
