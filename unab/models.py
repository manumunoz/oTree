from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Manu Munoz'

doc = """
Pilot UNAB
"""


class Constants(BaseConstants):
    name_in_url = 'unab'
    players_per_group = None
    num_rounds = 1
    instructions_template1 = 'unab/InstP1.html'
    instructions_template2 = 'unab/InstP2.html'
    instructions_template3 = 'unab/InstP3.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    anxious=models.IntegerField()
    secure=models.IntegerField()
    avoidant=models.IntegerField()

    a1 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a2 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a3 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a4 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a5 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a6 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a7 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a8 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a9 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a10 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a11 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a12 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a13 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a14 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a15 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a16 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a17 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a18 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a19 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a20 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a21 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a22 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a23 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a24 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a25 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a26 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a27 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a28 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a29 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a30 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a31 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a32 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a33 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a34 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a35 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a36 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a37 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a38 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a39 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a40 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a41 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)
    a42 = models.IntegerField(choices=[[0, 'F'], [1, 'V'], ], widget = widgets.RadioSelectHorizontal)

    def attachment_styles(self):
        self.anxious = self.a1 + self.a3 + self.a5 + self.a7 + self.a11 + self.a14 + self.a16 + self.a19 + self.a23 + \
                       self.a25 + self.a28 + self.a31 + self.a35 + self.a38 + self.a39
        self.secure = self.a2 + self.a8 + self.a12 + self.a13 + self.a17 + self.a20 + self.a22 + self.a26 + self.a29 + \
                       self.a33 + self.a36 + self.a40 + self.a42
        self.avoidant = self.a4 + self.a6 + self.a9 + self.a10 + self.a15 + self.a18 + self.a21 + self.a24 + self.a27 + \
                       self.a30 + self.a32 + self.a34 + self.a37 + self.a41

    n1 = models.StringField()
    n2 = models.StringField()
    n3 = models.StringField()
    n4 = models.StringField()
    n5 = models.StringField()

    c1 = models.IntegerField(choices=[0,1,2,3], widget = widgets.RadioSelectHorizontal)
    c2 = models.IntegerField(choices=[0,1,2,3], widget = widgets.RadioSelectHorizontal)
    c3 = models.IntegerField(choices=[0,1,2,3], widget = widgets.RadioSelectHorizontal)
    c4 = models.IntegerField(choices=[0,1,2,3], widget = widgets.RadioSelectHorizontal)
    c5 = models.IntegerField(choices=[0,1,2,3], widget = widgets.RadioSelectHorizontal)

    g1 = models.IntegerField(choices=[0,1,2,3], widget = widgets.RadioSelectHorizontal)
    g2 = models.IntegerField(choices=[0,1,2,3], widget = widgets.RadioSelectHorizontal)
    g3 = models.IntegerField(choices=[0,1,2,3], widget = widgets.RadioSelectHorizontal)
    g4 = models.IntegerField(choices=[0,1,2,3], widget = widgets.RadioSelectHorizontal)
    g5 = models.IntegerField(choices=[0,1,2,3], widget = widgets.RadioSelectHorizontal)
    g6 = models.IntegerField(choices=[0,1,2,3], widget = widgets.RadioSelectHorizontal)
    g7 = models.IntegerField(choices=[0,1,2,3], widget = widgets.RadioSelectHorizontal)
    g8 = models.IntegerField(choices=[0,1,2,3], widget = widgets.RadioSelectHorizontal)
    g9 = models.IntegerField(choices=[0,1,2,3], widget = widgets.RadioSelectHorizontal)
    g10 = models.IntegerField(choices=[0,1,2,3], widget = widgets.RadioSelectHorizontal)