from math import sqrt, atan2, degrees, sin, cos, pi
from random import randint, choice
from dialogues import *
from printer import cprint


# ------------------------------------------------- Player Object --------------------------------------------------- #


class Player(object):
    def __init__(self, name, health, inventory=None, position=None, vision=40):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.position = position
        self.vision = vision

    def get_position(self):
        return self.position

    def change_position(self, dx, dy):
        return self.position.d_pos(dx, dy)

    def get_surroundings(self, vision, objects):
        """
        :param vision: Integer representing the maximum distance to which the player may "see"
        :param objects: Dictionary containing objects and their coordinates. Given by Map.get_objects.
        :return: Returns a tuple containing tuples with the name of the object, distance from the object, and the
        cardinality relative to the position of the player.
        """
        in_range = ()
        pos = self.position
        for e in objects.keys():
            d = pos.distance(e)
            if d <= vision:
                in_range += ((objects[e], d, pos.cardinality(e)), )

        return in_range

    def __str__(self):
        vals = [self.name, self.health, self.inventory, self.position]
        stringrep = ""
        for e in vals:
            stringrep += str(e) + ", "

        return stringrep[:-2]

    def __repr__(self):
        return str((self.x, self.y))

# ------------------------------------------------- Space Objects --------------------------------------------------- #

class SpaceObject(object):
    def __init__(self, name=None, desc_vague=None, desc_detailed=None, scene=None):
        self.name = self.generate_name()
        self.header = self.generate_header()
        self.desc_vague = self.generate_desc_vague()
        self.desc_detailed = self.generate_desc_detailed()
        self.footer = self.generate_footer()
        self.scene = scene

    def inspect_vague(self):
        cprint(string=("OBJ - ID: " + self.name), t=0.20)
        cprint(string='. . . . . ', t=0.30)
        sleep(0.2)
        return (self.header +'\n'+ self.desc_vague)

    def inspect_detailed(self):
        cprint(string=("ID: " + self.name), t=0.20)
        cprint(string='. . . . . ', t=0.30)
        sleep(0.2)
        return self.header +'\n'+ self.desc_detailed +'\n'+ self.footer

    def generate_name(self):
        raise NotImplementedError

    def generate_header(self):
        raise NotImplementedError

    def generate_desc_vague(self):
        raise NotImplementedError

    def generate_desc_detailed(self):
        raise NotImplementedError

    def generate_footer(self):
        raise NotImplementedError

    def get_name(self):
        return self.name

    def get_desc_vague(self):
        return self.desc_vague

    def get_desc_detailed(self):
        return self.desc_detailed

    def __repr__(self):
        return self.name


class Artifact(SpaceObject):
    def __init__(self, name="Artifact"):
        super(Artifact, self).__init__(name=name)

    def generate_name(self):
        return generate_name(4, 4)

    def generate_header(self):
        return generate_dialogue((desc_artifact_header,))

    def generate_desc_vague(self):
        return generate_dialogue((desc_artifact_vague,))

    def generate_desc_detailed(self):
        return generate_dialogue((desc_artifact_detailed,))

    def generate_footer(self):
        return generate_dialogue((desc_artifact_footer,))


class Planet(SpaceObject):
    def __init__(self, name="Planet"):
        super(Planet, self).__init__(name=name)

    def generate_header(self):
        ## TODO
        pass

    def generate_desc_vague(self):
        ## TODO
        pass

    def generate_desc_detailed(self):
        ## TODO
        pass

    def generate_footer(self):
        ## TODO
        pass


class Star(SpaceObject):
    def __init__(self, name="Star"):
        super(Star, self).__init__(name=name)

    def generate_header(self):
        ## TODO
        pass

    def generate_desc_vague(self):
        ## TODO
        pass

    def generate_desc_detailed(self):
        ## TODO
        pass

    def generate_footer(self):
        ## TODO
        pass


class Wreckage(SpaceObject):
    def __init__(self, name="Wreckage"):
        super(Wreckage, self).__init__(name=name)

    def generate_header(self):
        ## TODO
        pass

    def generate_desc_vague(self):
        ## TODO
        pass

    def generate_desc_detailed(self):
        ## TODO
        pass

    def generate_footer(self):
        ## TODO
        pass



#
# a = Artifact()
# print a.inspect_vague()
# print a.inspect_detailed()
#
# s = []
# for e in xrange(10):
#     s.append(Artifact())
# for e in s:
#     print e.inspect_vague()
