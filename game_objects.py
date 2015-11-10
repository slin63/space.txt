# Handles objects (including the player)
# from math import sqrt, atan2, degrees

#
# class C(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def d_pos(self, dx, dy):
#         self.x += dx
#         self.y += dy
#
#     def get_x(self):
#         return self.x
#
#     def get_y(self):
#         return self.y
#
#     def distance(self, other):
#         dx = other.get_x() - self.x
#         dy = other.get_y() - self.y
#         return sqrt(dx**2 + dy**2)
#
#     def theta(self, other):
#         dx = other.get_x() - self.x
#         dy = other.get_y() - self.y
#         return degrees(atan2(dy, dx))
#
#     def cardinality(self, other):
#         theta = self.theta(other)
#         if theta <= 22.5:
#             direction = "E"
#         if 22.5 < theta <= 67.5:
#             direction = "NE"
#         if 67.5 < theta <= 112.5:
#             direction = "N"
#         if 112.5 < theta <= 157.5:
#             direction = "NW"
#         if 157.5 < theta <= 202.5:
#             direction = "W"
#         if 202.5 < theta <= 247.5:
#             direction = "SW"
#         if 247.5 < theta <= 292.5:
#             direction = "S"
#         if 292.5 < theta <= 337.5:
#             direction = "SE"
#         if 337.5 < theta:
#             direction = "E"
#         return direction
#
#     def __str__(self):
#         return str((self.x, self.y))
#
#     def __eq__(self, other):
#         return ((self.get_x(), self.get_y()),) == ((other.get_x(), other.get_y()),)
#
#     def __repr__(self):
#         return str((self.x, self.y))


class Player(object):
    def __init__(self, name, health, inventory=None, position=None, vision=20):
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
#
# obj_test = {
#     C(0, 0): 'STAR322B', C(4, 15): 'WRECK', C(12, 5): 'SAT', C(6, 15): 'SAT', C(12, 14): 'STAR353A', C(2, 18): 'WRECK',
#     C(14, 9): 'DEBRIS', C(10, 2): 'WRECK', C(13, 1): 'DEBRIS', C(12, 7): 'DEBRIS'
# }
#
# p = Player("p", 100, position=C(4, 6))
# print p.get_surroundings(8, obj_test)
#
# # a = C(0,0)
# b = C(3,4)
# print("Distance = %s" % a.distance(b))
# print("Theta = %s" % a.theta(b))
# print("Cardinality = %s" % a.cardinality(b))
