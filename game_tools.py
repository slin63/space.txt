from movement import *


def report_surroundings(mapobj, vision):
    surr = mapobj.player.get_surroundings(vision, mapobj.get_objects())
    # print(mapobj.get_objects())  # Gives all objects within the map object
    num_objs = len(surr)
    count = 1
    print("%s point(s) of interest nearby . . . " % num_objs)
    for obj in surr:
        distance = evaluate_distance(obj[1], vision)
        direction = obj[2]
        if distance == "same grid":
            print("\t%s. Located on current grid." % count)
        elif distance == "Barely detectable":
            print("\t%s. %s: %s(?)" % (count, distance, direction))
        else:
            print("\t%s. %s: %s" % (count, distance, direction))
        count += 1


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
        return "same grid"


def cardinal_to_dp(card, d_pos):
    card_coord = {
        "n": (0, d_pos), "e": (d_pos, 0), "s": (0, -d_pos),  "w": (-d_pos, 0),
        "ne": (d_pos * sin(pi/4), d_pos * cos(pi/4)), "nw": (-d_pos * sin(pi/4), d_pos * cos(pi/4)),
        "sw": (-d_pos * sin(pi/4), -d_pos * cos(pi/4)), "se": (d_pos * sin(pi/4), -d_pos * cos(pi/4)),
    }

    return card_coord[card]
