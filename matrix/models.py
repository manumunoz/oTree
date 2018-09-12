from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from random import randint


class Constants(BaseConstants):
    name_in_url = 'survey2'
    players_per_group = None
    num_rounds = 1
    male_names = ['John',"Rouben"]
    female_names = ['Anna','Maria']
    all_right_matrix = [[[randint(10, 99) for x in range(10)] for y in range(10)] for r in range(num_rounds)]
    all_left_matrix = [[[randint(10, 99) for x in range(10)] for y in range(10)] for r in range(num_rounds)]
    max_right = [max(sub_array) for sub_array in all_right_matrix]
    max_right = [max(sub_array) for sub_array in max_right]
    max_left = [max(sub_array) for sub_array in all_left_matrix]
    max_left = [max(sub_array) for sub_array in max_left]

class Subsession(BaseSubsession):
    pass







class Group(BaseGroup):
    pass


class Player(BasePlayer):

    sumOfMax = models.PositiveIntegerField(
        verbose_name = "Please sum the maximum numbers from Left and Right tables and insert in the box ",
        min=20, max=198
    )
    age = models.PositiveIntegerField(
        verbose_name='What is your age?',
        min=13, max=125)

    gender = models.CharField(
        choices= ['Male', 'Female'],
        verbose_name='What is your gender?',
        widget = widgets.RadioSelect)

    names = models.CharField(
        choices= [],
        verbose_name='Please select a name',
        widget = widgets.RadioSelect)

    crt_bat = models.PositiveIntegerField(
        verbose_name='''
        A bat and a ball cost 22 dollars in total.
        The bat costs 20 dollars more than the ball.
        How many dollars does the ball cost?'''
    )

    crt_widget = models.PositiveIntegerField(
        verbose_name='''
        "If it takes 5 machines 5 minutes to make 5 widgets,
        how many minutes would it take 100 machines to make 100 widgets?"
        '''
    )

    crt_lake = models.PositiveIntegerField(
        verbose_name='''
        In a lake, there is a patch of lily pads.
        Every day, the patch doubles in size.
        If it takes 48 days for the patch to cover the entire lake,
        how many days would it take for the patch to cover half of the lake?
        '''
    )
