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
    num_rounds = 1

    circle = 1 # Majority
    triangle = 0 # Minority
    names = ['1','2','3','4','5','6','7','8','9','10','11']
    # names_2 = ['5','7','9','11','2','4','6','8','10','1','3']
    names = ['1', '2', '3']
    attribute = [0,1,1,0,1,0,1,1,1,0,0]
    attributes = {'1': 0, '2': 1, '3': 1, '4': 0, '5': 1, '6': 0, '7': 1, '8': 1, '9': 1, '10': 0, '11': 0}
    position = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, '11': 11}
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    # visible = 1
    # invisible = 0
    players_per_group = len(names)


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
                p.is_circle = 1
                p.liked_action = 1
            else:
                p.given_type = 4 # triangle-triangle
                p.chosen_type = 4
                p.is_circle = 0
                p.liked_action = 0



class Group(BaseGroup):
    total_circles = models.IntegerField()
    total_triangles = models.IntegerField()
    total_up = models.IntegerField()
    total_down = models.IntegerField()
    network_data = models.LongStringField()

    def displaying_network(self):
        nodes = [{'data': {'id': i, 'name': i, 'action': self.get_player_by_id(i).action, 'shape': self.get_player_by_id(i).chosen_type,
                           'attribute': Constants.attributes[i], 'position': Constants.position[i]},  'group': 'nodes'} for i in Constants.names]
        edges = []
        elements = nodes + edges
        style = [{'selector': 'node', 'style': {'content': 'data(name)'}}]
        self.network_data = json.dumps({'elements': elements,
                                        'style': style,
                                        })

    def forming_network(self):
        nodes = [{'data': {'id': i, 'name': i, 'action': self.get_player_by_id(i).action, 'shape': self.get_player_by_id(i).chosen_type,
                           'attribute': Constants.attributes[i], 'position': Constants.position[i]}, 'group': 'nodes'} for i in Constants.names]
        edges = []
        for p in self.get_players():
            friends = json.loads(p.friends)
            edges.extend(
                [{'data': {'id': p.name + i, 'source': p.name, 'target': i}, 'group': 'edges'} for i in friends])

            # Copio el valor de las propuestas recogido en las variables con numbre (1,2,3,...) a
            # proo_to_1, prop_to_2, ...
            for i in friends:
                setattr(p, 'prop_to_' + i, getattr(p, i))

        elements = nodes + edges
        style = [{'selector': 'node', 'style': {'content': 'data(name)'}}]
        self.network_data = json.dumps({'elements': elements,
                                        'style': style,
                                        })

    def calculate_props_from_and_links(self):
        for player_to in self.get_players():
            for player_from in self.get_players():
                kiubo_prop_from = False
                kiubo_link = 0
                if player_from.name != player_to.name: # si no soy yo mismo
                    kiubo_prop_from = bool(getattr(player_from, 'prop_to_' + player_to.name)) # cojo el valor de la propuesta
                    if getattr(player_to, 'prop_to_' + player_from.name) == True and kiubo_prop_from == True:
                        kiubo_link = 1
                    else:
                        kiubo_link = 0
                else:
                    kiubo_link = 0 # link conmigo mismo = 1

                setattr(player_to, 'prop_from_' + player_from.name, kiubo_prop_from) # la añado a prop_from_X
                setattr(player_to, 'link_with_' + player_from.name, kiubo_link)

    # def calculate_actions(self):
    #     for player in self.get_players():
    #         for partner in self.get_players():
    #             choice = 0
    #             action_up = 0
    #             if player.name != partner.name: # si no soy yo mismo
    #                 action_up = partner.action
    #                 if action_up == 1:
    #                     choice = 1
    #                 else:
    #                     choice = 0
    #             setattr(player, 'action_' + partner.name, choice) # la añado a prop_from_X

    def calculate_actions(self):
        for player in self.get_players():
            for partner in self.get_players():
                action_up = partner.action
                if action_up == 1:
                    choice = 1
                else:
                    choice = 0
                setattr(player, 'action_' + partner.name, choice) # la añado a prop_from_X

    def summing_types(self):
        players = self.get_players()
        circles = [p.is_circle for p in players]
        self.total_circles = sum(circles)
        self.total_triangles = len(Constants.names)-self.total_circles

    def summing_choices(self):
        players = self.get_players()
        action_up = [p.action for p in players]
        self.total_up = sum(action_up)
        self.total_down = len(Constants.names) - self.total_up


# noinspection PyPackageRequirements
class Player(BasePlayer):
    given_symbol = models.BooleanField()
    # chosen_symbol = models.BooleanField()
    given_preference = models.BooleanField() # circle or triangle assigned exogenously
    # chosen_preference = models.BooleanField()  # circle or triangle chosen endogenously
    given_type = models.IntegerField() # combination of symbol and preference
    chosen_type = models.IntegerField() # combination of symbol and preference
    is_circle = models.IntegerField()
    action = models.IntegerField() # Reported belief on P3's verification
    liked_action = models.IntegerField()
    degree = models.IntegerField()
    coordination_score = models.IntegerField()
    coordination_gains = models.IntegerField()
    linking_costs = models.IntegerField()
    round_gains = models.IntegerField()

    def calculate_degree(self):
        self.degree = self.link_with_1 + self.link_with_2 + self.link_with_3
        # self.degree = self.link_with_1 + self.link_with_2 + self.link_with_3 + self.link_with_4 + self.link_with_5 + \
        #               self.link_with_6 + self.link_with_7 + self.link_with_8 + self.link_with_9 + self.link_with_10 +\
        #               self.link_with_11
        self.linking_costs = self.degree * Constants.link_cost

    def calculate_coordinate(self):
        if self.action == self.action_1:
            self.coordinate_1=1
        if self.action == self.action_2:
            self.coordinate_2=1
        if self.action == self.action_3:
            self.coordinate_3=1
        # if self.action == self.action_4:
        #     self.coordinate_4=1
        # if self.action == self.action_5:
        #     self.coordinate_5=1
        # if self.action == self.action_6:
        #     self.coordinate_6=1
        # if self.action == self.action_7:
        #     self.coordinate_7=1
        # if self.action == self.action_8:
        #     self.coordinate_8=1
        # if self.action == self.action_9:
        #     self.coordinate_9=1
        # if self.action == self.action_10:
        #     self.coordinate_10=1
        # if self.action == self.action_11:
        #     self.coordinate_11=1
        self.coordination_score = self.coordinate_1 + self.coordinate_2 + self.coordinate_3
        # self.coordination_score = self.coordinate_1 + self.coordinate_2 + self.coordinate_3 + self.coordinate_4  + \
        #                           self.coordinate_5 + self.coordinate_6 + self.coordinate_7 + self.coordinate_8 + \
        #                           self.coordinate_9 + self.coordinate_10 + self.coordinate_11
        if self.action == self.liked_action:
            self.coordination_gains = self.coordination_score * Constants.liked_gain
        else:
            self.coordination_gains = self.coordination_score * Constants.disliked_gain
        self.round_gains = self.coordination_gains - self.linking_costs
        self.payoff = self.round_gains

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


for i in Constants.names:
    Player.add_to_class(i, models.BooleanField(widget=widgets.CheckboxInput, blank=True))
    # Añado a Player las variables de propuestas con friendly names que luego rellenaremos
    Player.add_to_class('prop_to_' + i,  models.BooleanField(initial=0))
    Player.add_to_class('prop_from_' + i, models.BooleanField(initial=0))
    Player.add_to_class('link_with_' + i, models.IntegerField(initial=0))
    Player.add_to_class('action_' + i,  models.IntegerField(initial=0))
    Player.add_to_class('coordinate_' + i,  models.IntegerField(initial=0))

