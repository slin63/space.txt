# Handles player and scene locations
from random import randint, choice
from game_objects import Player
from math import sqrt, atan2, degrees


class Map(object):
    """Object representing both the overworld map and the superclass of unique locations
    within the overworld."""
    def __init__(self, size, objects, density=0.05, player=None):
        """Size is an intenger value representing the length of the square overworld.
           Objects is a list of possible objects that will spawn in this instance.
           Density represents the decimal probability of an object spawning in a given coordinate"""
        self.size = size
        self.objects = objects
        self.density = density
        self.player = player
        self.grid = self.populate_grid(size)

    def populate_grid(self, size):
        """Populates an empty dictionary with coordinate tuples
        and associates the coordinates with randomly selected objects from select_object."""
        grid = {}
        for i in range(size):
            y = 0
            for j in range(size):
                grid[C(i, y)] = self.select_object()
                y += 1

        return grid

    def select_object(self):
        """Uses randint to determine presence or absence of an object
        at a given coordinate when called by populate_grid."""
        if randint(0, 100) < (self.density*100):
            return choice(self.objects)
        else:
            return '-'

    def get_objects(self):
        obj_dic = {}
        for e in self.grid:
            if self.grid[e] != '-':
                obj_dic[e] = self.grid[e]
        return obj_dic

    def get_player_inters(self):
        pos = self.player.get_position()
        objs = self.get_objects()
        for e in objs.keys():
            if pos == e:
                return pos, objs[e]

    def get_player_info(self):
        return self.player

    def render_grid(self):
        """Renders the objects in the grid as a formatted string."""
        grid_l = []
        grid_s = ''
        count = 0

        for e in self.grid:
            grid_l += ((e, self.grid[e]),)

        for e in sorted(grid_l):
            grid_s += str(e) + ' '
            count += 1
            if count % self.size == 0:
                grid_s += "\n"

        return grid_s


class C(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def d_pos(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance(self, other):
        dx = other.get_x() - self.x
        dy = other.get_y() - self.y
        return sqrt(dx**2 + dy**2)

    def theta(self, other):
        dx = other.get_x() - self.x
        dy = other.get_y() - self.y
        return degrees(atan2(dy, dx))

    def cardinality(self, other):
        theta = self.theta(other)

        if theta <= 22.5:
            direction = "E"
        if 22.5 < theta <= 67.5:
            direction = "NE"
        if 67.5 < theta <= 112.5:
            direction = "N"
        if 112.5 < theta <= 157.5:
            direction = "NW"
        if 157.5 < theta <= 202.5:
            direction = "W"
        if 202.5 < theta <= 247.5:
            direction = "SW"
        if 247.5 < theta <= 292.5:
            direction = "S"
        if 292.5 < theta <= 337.5:
            direction = "SE"
        if 337.5 < theta:
            direction = "E"
        return direction

    def __str__(self):
        return str((self.x, self.y))

    def __eq__(self, other):
        return ((self.get_x(), self.get_y()),) == ((other.get_x(), other.get_y()),)

    def __repr__(self):
        return str((self.x, self.y))


#
random_objects = ['A', 'B', 'C', 'D']
p = Player("P", 100, ["item"], C(0, 0))
s = Map(20, random_objects, 0.05)
print(s.get_objects())
#
# print(s.get_player_inters())
# print(s.get_player_info())
#
# p.change_position(0, 2)
#
# print(s.get_player_inters())
# print(s.get_player_info())
#
# p.change_position(2, 0)
#
# print(s.get_player_inters())
# print(s.get_player_info())
#
# grid = s.render_grid()
#
# print(grid)
