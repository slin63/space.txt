"""Contains files for dialogue scene generation"""
## TODO: REPLACE PRINT WITH CPRINT()
from random import choice as ch  # This will cause issues I feel
from printer import cprint


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

    def list_room_contents(self, room):
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

    def list_room_contents(self, room):
        desc = None
        object_dic = None

        for e in self.rooms_desc:
            if e.lower() == room.lower():
                desc = self.rooms_desc[e]
                object_dic = self.rooms_objs[e]

        cprint(desc)
        cprint('You see the following: ')
        for obj in object_dic:
            cprint('\t' + obj)

        return object_dic


obj_control = {
    'control_object': 'control_obj_desc'
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

rooms_wreckage_desc = {
    'Control Room': 'You step inside the control room desc',
    'Observation Deck': 'You step inside the observ room desc',
    'Generator Room': 'You step inside the generator room desc',
    'Living Quarters': 'You step inside the quarters room desc'
}

rooms_wreckage_objs = {
    'Control Room': obj_control,
    'Observation Deck': obj_observ,
    'Generator Room': obj_gener,
    'Living Quarters': obj_quarters
}

wreckage_rooms = [
    (rooms_wreckage_desc, rooms_wreckage_objs)
]
