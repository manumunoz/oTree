from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'attached'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q2=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q3=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q4=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q5=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q6=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q7=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q8=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q9=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q10=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q11=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q12=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q13=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q14=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q15=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q16=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q17=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q18=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q19=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q20=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q21=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q22=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q23=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q24=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q25=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q26=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q27=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q28=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q29=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q30=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q31=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q32=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q33=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q34=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q35=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
    q36=models.IntegerField(
        choices=[
            [1, '1. Totalmente en desacuerdo'],
            [2, '2. En desacuerdo'],
            [3, '3. Levemente en desacuerdo'],
            [4, '4. Ni de acuerdo ni en desacuerdo'],
            [5, '5. Levemente de acuerdo'],
            [6, '6. De acuerdo'],
            [7, '7. Totalmente de acuerdo'],
        ],
    )
