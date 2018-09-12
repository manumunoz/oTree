from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'attached_en'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    q1=models.IntegerField(
        choices=[
            [1, 'Strongly Agree'],
            [2, 'Agree'],
            [3, 'Slightly Agree'],
            [4, 'Neither Agree nor Disagree'],
            [5, 'Slightly Disagree'],
            [6, 'Disagree'],
            [7, 'Strongly Disagree'],
        ],
        widget=widgets.RadioSelect
    )
    q2=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q3=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q4=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q5=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q6=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q7=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q8=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q9=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q10=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q11=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q12=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q13=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q14=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q15=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q16=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q17=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q18=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q19=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q20=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q21=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q22=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q23=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q24=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q25=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q26=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q27=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q28=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q29=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q30=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q31=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q32=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q33=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q34=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q35=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
    q36=models.IntegerField(
        choices=[0,1,2,3,4,5],
    )
