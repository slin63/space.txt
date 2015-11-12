from game_tools import *
from time import time


def main(map_size, density, object_base, debug=False):
    p = Player("P", 100, ["item"], C(0,0))
    start = time()
    world = Map(map_size, object_base, density, player=p)
    end = time()
    init_time = str(end - start)
    map_objects = world.get_objects()

    if debug:
        print("# DEBUG : \n\tMAP_SIZE = %s x %s\n\tINIT_TIME = %s\n\tNUM_OBJECTS = %s\n\tSURROUNDINGS = %s\n"
              % (map_size, map_size, init_time, len(map_objects), p.get_surroundings(world.player.vision, map_objects)))

    while 1 == 1:
        report_surroundings(world, world.player.vision)
        esc = True

        while esc:
            surroundings = world.player.get_surroundings(vision=world.player.vision, objects=map_objects)
            # print(surroundings)
            # print(map_objects)

            # cls()

            cprint("Options:\n\tm - Move\n\tc - Check ship status\n\ti - Investigate grid\n\ts - Survey\n\t"
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
                investigate(surroundings, world.player.vision)
            elif ans.lower() == 'p':
                report_personal_status(world)
            elif ans.lower() == 'z':
                player_sleep(world)
            elif ans.lower() == 'd':
                cprint("You survived ##TODO days")
                brief_pause("Enter to exit . . .")
                exit()


random_objects = [Artifact]
p = Player("P", 100, ["item"], C(0,0))
s = Map(5, random_objects, 0.05, player=p)


if __name__ == "__main__":
    cprint("EGG-SPACE.TXT 0.11.12")
    main(
        map_size=2,
        density=0.5,
        object_base=random_objects,
        debug=True
    )


