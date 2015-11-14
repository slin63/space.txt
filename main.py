from game_tools import *
from time import time


def main(map_size, density, object_base, debug=False):
    p = Player("P", 100, [], C(0, 0))
    start = time()
    world = Map(map_size, object_base, density, player=p)
    end = time()
    init_time = str(end - start)
    map_objects = world.get_objects()

    if debug:
        print("# DEBUG : \n\tMAP_SIZE = %s x %s\n\tINIT_TIME = %s\n\tNUM_OBJECTS = %s\n\tSURROUNDINGS = %s\n"
              % (map_size, map_size, init_time, len(map_objects), p.get_surroundings(world.player.vision, map_objects)))

    while 1 == 1:

        esc = True

        while esc:

            print world.player.encounters

            get_date(world)
            report_surroundings(world, world.player.vision)
            surroundings = world.player.get_surroundings(vision=world.player.vision, objects=map_objects)

            cprint("Options:\n\tm - Move\n\tc - Check ship status\n\ti - Investigate objects\n\ts - Survey\n\t"
                   "p - Check personal status\n\tz - Sleep\n\td - Die", 0.01)
            ans = raw_input()

            if ans.lower() == 'm':
                move_player(world)
                esc = False

            elif ans.lower() == 'c':
                report_status(world)
            elif ans.lower() == 's':
                report_surroundings(world, world.player.vision)
            elif ans.lower() == 'i':
                investigate_menu(surroundings, world.player.vision, world)
            elif ans.lower() == 'p':
                report_personal_status(world)
            elif ans.lower() == 'z':
                player_sleep(world)
            elif ans.lower() == 'd':
                player_die(world)
                brief_pause("Enter to exit . . .")
                exit()

RANDOM_OBJECTS = [Wreckage]
# RANDOM_OBJECTS = [Artifact, Wreckage]
p = Player("P", 100, ["item"], C(0,0))
s = Map(5, RANDOM_OBJECTS, 0.05, player=p)

# s.player.position
# s.get_closest_obj()

if __name__ == "__main__":
    cls()
    cprint("EGG-SPACE.TXT 0.11.13")
    main(
        map_size=2,
        density=1,
        object_base=RANDOM_OBJECTS,
        debug=False,
    )

#
