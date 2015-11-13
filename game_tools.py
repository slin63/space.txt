from movement import *
from math import log


# ----------------------------------- Player control functions ---------------------------------------- #


def compact_dream_travel(world, days=1, do_dream=True):
    if do_dream:
        dream(world, days)
    change_date(world, days)
    brief_pause()
    return 0


def move_player(mapobj):
    direction = raw_input("Direction: ")
    magnitude = raw_input("For how long? (Days): ")
    d_pos = cardinal_to_dp(direction.lower(), float(magnitude))
    mapobj.player.change_position(d_pos[0], d_pos[1])
    sleep(0.5)
    cprint("Moving %s . . ." % (direction.upper()))
    compact_dream_travel(world=mapobj, days=int(magnitude))
    return 0


def report_status(mapobj):
    sleep(0.5)
    cprint("Fuel = %s, Position = %s" % (mapobj.player.health, mapobj.player.position))
    brief_pause()
    return 0


def report_surroundings(mapobj, vision):
    """Prints out a nice summary of the objects within vision of the player."""
    surr = mapobj.player.get_surroundings(vision, mapobj.get_objects())
    num_objs = len(surr)
    count = 1
    print("%s point(s) of interest nearby . . . " % num_objs)
    sleep(0.5)

    for obj in surr:
        distance = evaluate_distance(obj[1], vision)
        direction = obj[2]
        if distance.lower() == "same grid":
            cprint(string=("\t%s. Located on current grid." % count), t=0.022)
        elif distance == "Barely detectable":
            cprint(string=("\t%s. %s: %s(?)" % (count, distance, direction)), t=0.022)
        else:
            cprint(string=("\t%s. %s: %s" % (count, distance, direction)), t=0.022)
        count += 1

    brief_pause()
    return 0


def investigate(surroundings, vision, mapobj):
    count = 1
    if len(surroundings) == 0:  # When there's nothing around but empty space
        sleep(0.5)
        print make_border()
        cprint(string=random_dialogue(investigate_space), t=0.03)
        print make_border()
        brief_pause()
        return 0

    cprint("Select an object:")

    for obj in surroundings:
        distance = evaluate_distance(obj[1], vision)
        direction = obj[2]
        cprint(string=("\t%s. %s: %s" % (count, distance, direction)), t=0.022)
        count += 1

    print(make_border())

    ans = raw_input()

    ans_obj = surroundings[int(ans)-1]

    if ans_obj[1] == 0:
        sleep(0.5)
        print make_border()
        cprint(string=ans_obj[0].inspect_detailed(), t=0.03)
        mapobj.player.encounters.append(ans_obj[0])
        print make_border()

    else:
        sleep(0.5)
        print make_border()
        cprint(string=ans_obj[0].inspect_vague(), t=0.03)
        print make_border()

    compact_dream_travel(mapobj)

    return 0


def report_personal_status(world):
    ## TODO
    pass


def player_sleep(mapobj):
    ## TODO: IMPLEMENT DREAMING WHEN TRAVELING / SLEEPING
    cprint("How many days would you like to sleep for?: ", t=0.03)
    days = int(raw_input())
    cprint("Zzz . . . ", t=0.20)
    compact_dream_travel(world=mapobj, days=days)


def player_die(world):
    adj1 = choice(choice(adjectives_lists))
    adj2 = choice(choice(adjectives_lists))
    adj3 = choice(choice(adjectives_lists))
    world.egg_time.print_time_elapsed()
    num_encounters = len(world.player.encounters)
    num_dreams = len(world.player.dreams)
    cprint(string="You had %s encounter(s) and %s dream(s)." % (num_encounters, num_dreams))
    cprint(string="Your journey was . . . %s, %s, and %s. " % (adj1, adj2, adj3))

# ----------------------------------- Navigation and movement functions ---------------------------------------- #


def evaluate_distance(distance, vision):
    ratio = distance/vision
    if 0.7 < ratio <= 1.0:
        return "Barely detectable"
    if 0.5 < ratio <= 0.7:
        return "Distant"
    if 0.3 < ratio <= 0.5:
        return "Within reach"
    if 0 < ratio <= 0.3:
        return "Visibly near"
    if ratio == 0:
        return "Same grid"


def cardinal_to_dp(card, d_pos):
    card_coord = {
        "n": (0, d_pos), "e": (d_pos, 0), "s": (0, -d_pos),  "w": (-d_pos, 0),
        "ne": (2*d_pos * sin(pi/4), 2*d_pos * cos(pi/4)), "nw": (-2*d_pos * sin(pi/4), 2*d_pos * cos(pi/4)),
        "sw": (-2*d_pos * sin(pi/4), -2*d_pos * cos(pi/4)), "se": (2*d_pos * sin(pi/4), -2*d_pos * cos(pi/4)),
    }

    return card_coord[card]


def get_date(world):
    world.egg_time.print_date()
    return 0


def change_date(world, days=1):
    world.egg_time.change_date(days)


# -------------------------------------------- Player Status Functions --------------------------------------------- #


def dream(world, days=1, dream_chance=15):
    roll = randint(0, 100)
    if days == 2.713:
        dream_chance *= log(days)
    else:
        dream_chance += days
    # print dream_chance
    if roll < dream_chance:
        if Artifact in world.player.encounters:
            dream_string = world.player.generate_dream(dreams_terror)
            cprint('You have a dream . . . ', t=0.10)
            cprint(dream_string)
        else:
            dream_string = world.player.generate_dream(dreams_normal)
            cprint('You have a dream . . . ', t=0.10)
            cprint(dream_string)

    return 0


# random_objects = [Artifact]
# p = Player("P", 100, ["item"], C(0,0))
# s = Map(5, random_objects, 0.05, player=p)
#
#
# p.encounters.append(Artifact())

# l = [Artifact()]
# print Artifact in l

# print dream(s, 8)
