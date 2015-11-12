from movement import *
from printer import cprint


# ----------------------------------- Player control functions ---------------------------------------- #


def move_player(mapobj):
    direction = raw_input("Direction: ")
    magnitude = raw_input("Distance: ")
    d_pos = cardinal_to_dp(direction.lower(), float(magnitude))
    mapobj.player.change_position(d_pos[0], d_pos[1])
    sleep(0.5)
    cprint("Moving %s units %s." % (magnitude, direction.upper()))
    brief_pause()
    return 0


def report_status(mapobj):
    sleep(0.5)
    cprint("Fuel = %s, Position = %s" % (mapobj.player.health, mapobj.player.position))
    brief_pause()
    return 0


def report_surroundings(mapobj, vision):
    """Prints out a nice summary of the objects within vision of the player."""
    surr = mapobj.player.get_surroundings(vision, mapobj.get_objects())
    # print(mapobj.get_objects())  # Gives all objects within the map object
    num_objs = len(surr)
    count = 1
    print("%s point(s) of interest nearby . . . " % num_objs)
    sleep(0.5)
    for obj in surr:
        distance = evaluate_distance(obj[1], vision)
        direction = obj[2]
        if distance.lower() == "same grid":
            cprint(string=("\t%s. Located on current grid." % count), t=0.03)
        elif distance == "Barely detectable":
            cprint(string=("\t%s. %s: %s(?)" % (count, distance, direction)), t=0.03)
        else:
            cprint(string=("\t%s. %s: %s" % (count, distance, direction)), t=0.03)
        count += 1
    brief_pause()
    return 0


def investigate(surroundings, vision):
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
        cprint(string=("\t%s. %s: %s" % (count, distance, direction)))
        count += 1

    print(make_border())

    ans = raw_input()

    ans_obj = surroundings[int(ans)-1]
    if ans_obj[1] == 0:
        sleep(0.5)
        print make_border()
        cprint(string=ans_obj[0].inspect_detailed(), t=0.03)
        print make_border()
        brief_pause()
    else:
        sleep(0.5)
        print make_border()
        cprint(string=ans_obj[0].inspect_vague(), t=0.03)
        print make_border()
        brief_pause()
    return 0


def report_personal_status(world):
    ## TODO
    pass


def player_sleep(world):
    ## TODO
    pass

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
