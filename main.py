from game_tools import *
from time import time

## TODO: WORKING TITLE == "EGG SPACE"

# random_objects = [Wreckage(), Star(), Planet(), Artifact()]

random_objects = [Artifact]

def main(map_size, density):
    p = Player("P", 100, ["item"], C(0,0))
    start = time()
    world = Map(map_size, random_objects, density, player=p)
    end = time()
    init_time = str(end - start)[0:3]
    map_objects = world.get_objects()

    print("# DEBUG : \n\tMAP_SIZE = %s x %s\n\tINIT_TIME = %s\n\tNUM_OBJECTS = %s\n\tSURROUNDINGS = %s\n"
          % (map_size, map_size, init_time, len(map_objects), p.get_surroundings(world.player.vision, map_objects)))

    while 1 == 1:
        report_surroundings(world, world.player.vision)
        esc = True

        while esc:
            surroundings = world.player.get_surroundings(vision=world.player.vision, objects=map_objects)
            # print(surroundings)
            # print(map_objects)

            ans = raw_input("Options:\n\tm - Move\n\tc - Check ship status\n\ti - Investigate grid\n\ts - Survey\n\t")

            if ans.lower() == 'm':
                move_player(world)
                esc = False
            elif ans.lower() == 'c':
                report_status(world)
            elif ans.lower() == 's':
                report_surroundings(world, world.player.vision)
            elif ans.lower() == 'i':
                investigate(surroundings, world.player.vision)


p = Player("P", 100, ["item"], C(0,0))
s = Map(5, random_objects, 0.05, player=p)


main(20, 0.005)


