from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import numpy

class Constants(BaseConstants):
    name_in_url = 'sum_task'
    players_per_group = None
    num_rounds = 40
    max_rand = 99
    min_rand = 40
    num_rows = 10
    num_cols = 10

# min and max values for the rand_left & rand_right are good, but the other numbers should be all two-digits

class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    rand_left = models.PositiveIntegerField()
    rand_right = models.PositiveIntegerField()
    solution = models.PositiveIntegerField()
    answer = models.PositiveIntegerField()
    answer_correct = models.PositiveIntegerField(initial=0)
    num_correct = models.PositiveIntegerField(initial=0)
    m_left = numpy.zeros((Constants.num_rows, Constants.num_cols))
    m_right = numpy.zeros((Constants.num_rows, Constants.num_cols))

    def initialize(self):
        self.num_correct = sum([p.answer_correct for p in self.in_all_rounds()])
        self.rand_left = random.randint(Constants.min_rand, Constants.max_rand)
        self.rand_right = random.randint(Constants.min_rand, Constants.max_rand)
        self.solution = self.rand_left + self.rand_right

        for i in range(Constants.num_rows):
            for j in range(Constants.num_cols):
                self.m_left[i][j] = random.randint(0, self.rand_left - 1)
                self.m_right[i][j] = random.randint(0, self.rand_right - 1)

        self.m_left[random.randint(0, Constants.num_rows - 1)][random.randint(0, Constants.num_cols - 1)] = self.rand_left
        self.m_right[random.randint(0, Constants.num_rows - 1)][random.randint(0, Constants.num_cols - 1)] = self.rand_right

    def set_payoff(self):
        self.payoff=self.answer_correct
