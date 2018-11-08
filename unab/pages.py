from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Start(Page):
    pass

class Attach1(Page):

    form_model = 'player'
    form_fields = ['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12']

class Attach2(Page):

    form_model = 'player'
    form_fields = ['a13','a14','a15','a16','a17','a18','a19','a20','a21','a22','a23','a24']

class Attach3(Page):

    form_model = 'player'
    form_fields = ['a25','a26','a27','a28','a29','a30','a31','a32','a33','a34','a35','a36']

class Attach4(Page):

    form_model = 'player'
    form_fields = ['a37','a38','a39','a40','a41','a42']

    def before_next_page(self):
        self.player.attachment_styles()


class Network1(Page):

    form_model = 'player'
    form_fields = ['n1','n2','n3','n4','n5']

class Network2(Page):

    form_model = 'player'
    form_fields = ['c1','c2','c3','c4','c5']

class Network3(Page):

    form_model = 'player'
    form_fields = ['g1','g2','g3','g4','g5','g6','g7','g8','g9','g10']

class Code(Page):
    pass

page_sequence = [
    Start,
    Attach1,
    Attach2,
    Attach3,
    Attach4,
    Network1,
    Network2,
    Network3,
    Code,
]
