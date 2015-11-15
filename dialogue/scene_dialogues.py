"""Contains files for dialogue scene generation"""
## TODO: REPLACE PRINT WITH CPRINT()
from random import choice as ch  # This will cause issues I feel


class SceneRooms(object):
    def __init__(self, name):
        self.name = name

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
        self.rooms_desc_objs = self.select_rooms()

        self.rooms_wreckage_desc = self.rooms_desc_objs[0]
        self.rooms_wreckage_objs = self.rooms_desc_objs[1]

        # self.obj_control = {
        #     'control_object': 'control_obj_desc'
        # }
        #
        # self.obj_observ = {
        #     'observ_object': 'observ_obj_desc'
        # }
        #
        # self.obj_gener = {
        #     'gener_object': 'gener_obj_desc'
        # }
        #
        # self.obj_quarters = {
        #     'quarters_object': 'quarters_obj_desc'
        # }
        #
        # self.rooms_wreckage_desc = {
        #     'Control Room': 'You step inside the control room desc',
        #     'Observation Deck': 'You step inside the observ room desc',
        #     'Generator Room': 'You step inside the generator room desc',
        #     'Living Quarters': 'You step inside the quarters room desc'
        # }
        #
        # self.rooms_wreckage_objs = {
        #     'Control Room': self.obj_control,
        #     'Observation Deck': self.obj_observ,
        #     'Generator Room': self.obj_gener,
        #     'Living Quarters': self.obj_quarters
        # }
    def select_rooms(self):
        return ch(wreckage_rooms)
        pass

    def list_rooms(self):
        for room in self.rooms_wreckage_objs.keys():
            print('\t' + room)

    def list_room_contents(self, room):
        for e in self.rooms_wreckage_desc:
            if e.lower() == room.lower():
                desc = self.rooms_wreckage_desc[e]
                object_dic = self.rooms_wreckage_objs[e]

        print desc
        print 'You see the following: '
        for obj in object_dic:
            print '\t' + obj

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





