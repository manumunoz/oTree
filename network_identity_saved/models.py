from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from collections import OrderedDict
import json

author = 'Manu Munoz'

doc = """
Network Identity
"""


class Constants(BaseConstants):
    name_in_url = 'network_identity'
    num_rounds = 2
    players_per_group = 3

    circle = 1 # Majority
    triangle = 0 # Minority
    # names_1 = ['1','2','3','4','5','6','7','8','9','10','11']
    # names_2 = ['5','7','9','11','2','4','6','8','10','1','3']
    names = ['1', '2', '3']
    attribute = [0,1,1,0,1,0,1,1,1,0,0]
    attributes = {'1': 0, '2': 1, '3': 1, '4': 0, '5': 1, '6': 0, '7': 1, '8': 1, '9': 1, '10': 0, '11': 0}
    # visible = 1
    # invisible = 0

class Subsession(BaseSubsession):
    def creating_session(self):
        num_players_err = 'Too many participants for such a short name list'
        # the following may create issues with mTurk sessions where num participants is doubled
        assert len(Constants.names) <= self.session.num_participants, num_players_err
        for g in self.get_groups():
            cur_names = Constants.names.copy()
            # random.shuffle(cur_names)
            for i, p in enumerate(g.get_players()):
                p.name = cur_names[i]
        for p in self.get_players():
            p.given_symbol = bool(Constants.attribute[p.id_in_group - 1])
            p.given_preference = bool(Constants.attribute[p.id_in_group - 1])
            if p.given_symbol == 1 and p.given_preference == 1:
                p.given_type = 1  # circle-circle
                p.chosen_type = 1
            else:
                p.given_type = 4 # triangle-triangle
                p.chosen_type = 4

class Group(BaseGroup):
    network_data = models.LongStringField()

    def displaying_network(self):
        nodes = [{'data': {'id': i, 'name': i, 'action': self.get_player_by_id(i).action, 'shape': self.get_player_by_id(i).chosen_type,
                           'attribute': Constants.attributes[i]},  'group': 'nodes'} for i in Constants.names]
        edges = []
        elements = nodes + edges
        style = [{'selector': 'node', 'style': {'content': 'data(name)'}}]
        self.network_data = json.dumps({'elements': elements,
                                        'style': style,
                                        })

    def forming_network(self):
        nodes = [{'data': {'id': i, 'name': i, 'action': self.get_player_by_id(i).action, 'shape': self.get_player_by_id(i).chosen_type,
                           'attribute': Constants.attributes[i]}, 'group': 'nodes'} for i in Constants.names]
        edges = []
        for p in self.get_players():
            friends = json.loads(p.friends)
            edges.extend(
                [{'data': {'id': p.name + i, 'source': p.name, 'target': i}, 'group': 'edges'} for i in friends])


        #
        # for receiver in players
        #   prop_received = []
        #   for proposer in players:
        #      if propser != sender:
        #         if receiver in proposer.friends:
        #              prop_received.append(proposer.name)
        #   receiver.props_from = str(prop_received)

        elements = nodes + edges
        style = [{'selector': 'node', 'style': {'content': 'data(name)'}}]
        self.network_data = json.dumps({'elements': elements,
                                        'style': style,
                                        })


class Player(BasePlayer):
    given_symbol = models.BooleanField()
    # chosen_symbol = models.BooleanField()
    given_preference = models.BooleanField() # circle or triangle assigned exogenously
    # chosen_preference = models.BooleanField()  # circle or triangle chosen endogenously
    given_type = models.IntegerField() # combination of symbol and preference
    chosen_type = models.IntegerField() # combination of symbol and preference
    action = models.BooleanField() # Reported belief on P3's verification

    # # Symbol Assignation
    # def assign_values(self):
    #     self.given_symbol = bool(Constants.attribute[self.id_in_group - 1])
    #     self.given_preference = bool(Constants.attribute[self.id_in_group - 1])
    #
    # # Given-Type Assignation
    # def assign_types(self):
    #     if self.given_symbol == 1 and self.given_preference == 1:
    #         self.given_type = 1  # circle-circle
    #         self.chosen_type = 1
    #     else:
    #         self.given_type = 4 # triangle-triangle
    #         self.chosen_type = 4

    # ONLY FOR PART 2!!!
    # # Chosen-Type Assignation if INCONSISTENT (should be different if consistent || invisible)
    # def update_values(self):
    #     if self.round_number == 1:
    #         self.chosen_type = self.given_type
    #     else:
    #         self.chosen_preference = self.player.in_round(self.round_number - 1).chosen_preference
    #         if self.given_type == 1 and self.chosen_preference == 1:
    #             self.chosen_type = 1 # circle-circle
    #         elif self.given_type == 1 and self.chosen_preference == 0:
    #             self.chosen_type = 2 # circle-triangle
    #         elif self.given_type == 4 and self.chosen_preference == 1:
    #             self.chosen_type = 3 # triangle-circle
    #         else:
    #             self.chosen_type = 4 # triangle-triangle

    name = models.StringField()
    friends = models.LongStringField()
    proposals_from = models.LongStringField()


for i in Constants.names:
    Player.add_to_class(i, models.BooleanField(widget=widgets.CheckboxInput, blank=True))
















