"""Contains files for dialogue scene generation"""
## TODO: REPLACE PRINT WITH CPRINT()
from random import choice as ch  # This will cause issues I feel
from printer import cprint
from dialogues import *

class SceneRooms(object):
    def __init__(self, name):
        self.name = name
        self.rooms_desc_objs = self.select_rooms()
        self.rooms_desc = self.rooms_desc_objs[0]
        self.rooms_objs = self.rooms_desc_objs[1]

    def select_rooms(self):
        raise NotImplementedError

    def list_rooms(self):
        raise NotImplementedError

    def introduce_room_contents(self, room):
        raise NotImplementedError

    @staticmethod
    def get_obj_desc(object_dic, obj):
        desc = None
        for e in object_dic:
            if e.lower() == obj.lower():
                desc = object_dic[e]

        return desc


class WreckageRooms(SceneRooms):
    def __init__(self):
        super(WreckageRooms, self).__init__(name='WreckageRooms')

    def select_rooms(self):
        return ch(wreckage_rooms)

    def list_rooms(self):
        for room in self.rooms_objs.keys():
            print('\t' + room)

    def introduce_room_contents(self, room):
        desc = None
        object_dic = None

        for e in self.rooms_desc:
            if e.lower() == room.lower():
                desc = self.rooms_desc[e]
                # print desc
                object_dic = self.rooms_objs[e]

        cprint(desc)
        cprint('You see the following: ')
        for obj in object_dic:
            cprint('\t' + obj)

        return object_dic

    def list_room_contents(self, room):
        object_dic = None

        for e in self.rooms_desc:
            if e.lower() == room.lower():
                object_dic = self.rooms_objs[e]

        for obj in object_dic:
            cprint('\t' + obj)


obj_control = {   # reflect on past ???
    "Captain's seat": 'Located inside a cramped hallway lined with toggles, switches, and holographic displays, '
                      'the pilot would have spent most of his time here directing crewmen elsewhere in the ship. '
                      '%s '
                      % (ch(adj_strange)),
    "Small window": "The windows in the cabin were kept small to prevent structural failures in the most populated "
                    "area of the vessel. There is very little to look at. ",
    "Your ship": "You peer through the small window and spot your own ship. It is alien in form, a vaguely spherical "
                 "object floating alone through unpopulated space. It was originally a satellite designed to travel "
                 "%s distances by accelerating ions to %s speeds. In %s it was re-purposed as an "
                 "exploratory vessel to be sold for consumer use. You feel embarrassed. "
                 % (ch(adj_large), ch(adj_pos), ch(random_number)),
    "Overhead display": "A masterwork of machine-weaving and light, the overhead display is formed of a network of "
                        "ultra-light fibers woven into a fine mesh. The fibers are dynamically "
                        "lit by a neighboring computer to project %s three dimensional images to the crew. "
                        "It is protected by a thick sheet of glass. "
                        % (ch(adj_pos)),
}

obj_observ = {
    'observ_object': 'observ_obj_desc'
}

obj_gener = {
    'gener_object': 'gener_obj_desc'
}

obj_quarters = {
    'quarters_object': 'quarters_obj_desc'
}

rooms_wreckage_desc_1 = {
    'Control Room': 'You step inside the control room. Every inch of the chamber is lined with rich technology and '
                    'elegant equipment. It is a far cry from your minimal cockpit. ',
    'Observation Deck': 'You step inside the observation deck. The room is circular, lined with fine chairs and '
                        'Earth paintings. The windows are undamaged and expose half of the room to the expansive '
                        'void outside. ',
    'Generator Room': "You step inside the generator room. The ship's main drive core is surrounded by an infinite"
                      "series of tubes and heatsink applicators. The drive's radioactive coolant is nowhere "
                      "to be found. You are awed by its sophistication.",
    'Living Quarters': 'You step inside the living quarters. Countless beds rest uselessly down a lengthy hallway. '
                       'Each mattress is equipped with a set of restraints and a velcro pillow. '
}

rooms_wreckage_objs_1 = {
    'Control Room': obj_control,
    'Observation Deck': obj_observ,
    'Generator Room': obj_gener,
    'Living Quarters': obj_quarters
}

wreckage_rooms = [
    (rooms_wreckage_desc_1, rooms_wreckage_objs_1)
]


