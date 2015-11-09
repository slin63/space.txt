# Handles player and scene locations
from random import randint, choice


class Map(object):
    """Object representing both the overworld map and the superclass of unique locations
    within the overworld."""
    def __init__(self, size, objects, density=0.05):
        """Size is an intenger value representing the length of the square overworld.
           Objects is a list of possible objects that will spawn in this instance.
           Density represents the decimal probability of an object spawning in a given coordinate"""
        self.size = size
        self.objects = objects
        self.density = density
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
            return ' '

    def render_grid(self):
        """Renders the objects in the grid as a formatted string."""
        grid = self.grid.keys()
        grid_s = ""

        count = 0
        while count < self.size:
            for i in grid:
                if i.get_x() == count:
                    grid_s += str(self.grid[i])
            count += 1
            grid_s += "\n"

        return grid_s


class C(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return str((self.x, self.y))


random_objects = ['A', 'B', 'C', 'D', 'E']

s = Map(20, random_objects, 0.05)

print(s.render_grid())
