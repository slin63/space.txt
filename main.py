from game_tools import *
from time import time


# random_objects = [Wreckage(), Star(), Planet(), Artifact()]

random_objects = [SpaceObject()]


def main(map_size, density):
    p = Player("P", 100, ["item"], C(0,0))
    start = time()
    s = Map(map_size, random_objects, density, player=p)
    end = time()
    init_time = str(end - start)[0:3]
    map_objects = s.get_objects()

    print("# DEBUG : \n\tMAP_SIZE = %s x %s\n\tINIT_TIME = %s\n\tNUM_OBJECTS = %s\n\tSURROUNDINGS = %s\n"
          % (map_size, map_size, init_time, len(map_objects), p.get_surroundings(s.player.vision, map_objects)))

    while 1 == 1:
        report_surroundings(s, s.player.vision)
        esc = True

        while esc:
            surroundings = s.player.get_surroundings(vision=s.player.vision, objects=map_objects)
            # print(surroundings)

            ans = raw_input("Options:\n\tm - Move\n\tc - Check ship status\n\ti - Investigate grid\n\ts - Survey\n\t")

            if ans.lower() == 'm':
                player_move(s)
                esc = False
            elif ans.lower() == 'c':
                print("Fuel = %s, Position = %s" % (s.player.health, s.player.position))
            elif ans.lower() == 's':
                report_surroundings(s, s.player.vision)
            elif ans.lower() == 'i':
                investigate(surroundings, s.player.vision)


p = Player("P", 100, ["item"], C(0,0))
s = Map(5, random_objects, 0.05, player=p)


main(600, 0.001)


