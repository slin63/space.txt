# Handles objects (including the player)


class Player(object):
    def __init__(self, name, health, inventory=[], position=None):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.position = position


s = Player("yes", 100, ["dog"])

print(s.name, s.health, s.inventory, s.position)





