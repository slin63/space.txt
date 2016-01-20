from game_tools import *
from time import time


def main(map_size, density, object_base, debug=False):
    p = Player("P", 100, [], C(map_size / 2, map_size / 2))
    start = time()
    world = Map(map_size, object_base, density, player=p)
    end = time()
    init_time = str(end - start)
    map_objects = world.get_objects()

    intro(p, 0.10)

    if debug:
        print("# DEBUG : \n\tMAP_SIZE = %s x %s\n\tINIT_TIME = %s\n\tNUM_OBJECTS = %s"
              "\n\tSURROUNDINGS = %s\n\tOBJECTS = %s"
              % (map_size, map_size, init_time, len(map_objects), p.get_surroundings(world.player.vision, map_objects),
                 map_objects))

    while 1 == 1:

        esc = True

        while esc:

            get_date(world)
            report_surroundings(world, p.vision)
            surroundings = world.player.get_surroundings(vision=p.vision, objects=map_objects)

            cprint("Options:\n\tm - Move\n\tc - Check ship status\n\ti - Investigate objects\n\ts - Survey\n\t"
                   "p - Check personal status\n\tz - Sleep\n\td - Die", 0.01)
            ans = raw_input()

            if ans.lower() == 'm':
                move_player(world)
                esc = False
            elif ans.lower() == 'c':
                report_ship_status(world)
            elif ans.lower() == 's':
                report_surroundings(world, p.vision)
            elif ans.lower() == 'i':
                investigate_space_menu(surroundings, p.vision, world)
            elif ans.lower() == 'p':
                report_personal_status(world)
            elif ans.lower() == 'z':
                player_sleep(world)
            elif ans.lower() == 'd':
                player_die(world)


# RANDOM_OBJECTS = [Artifact, Wreckage, Planet, Star]
RANDOM_OBJECTS = [Wreckage, Artifact]
p = Player("P", 100, ["item"], C(0,0))
s = Map(5, RANDOM_OBJECTS, 0.05, player=p)

if __name__ == "__main__":
    cls()

    main(
        map_size=1000,
        density=0.0001,
        object_base=RANDOM_OBJECTS,
        debug=False,
    )

# -------- Testing
#
# a = WreckageRooms()
# print a.rooms_wreckage_desc
# print a.rooms_wreckage_objs