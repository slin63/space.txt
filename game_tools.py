from movement import *
from math import log


# ------------------ Introduction

def intro(p, t=0.10):
    cprint("EGG-SPACE.TXT 0.11.13", t)
    cprint("You are %s years old. " % p.get_age_years(), t)
    year = p.get_date_till_death()[0]
    days = p.get_date_till_death()[1]
    if year > 1:
        cprint("In %s years and %s days, you will die. " %
               (p.get_date_till_death()[0], p.get_date_till_death()[1]), t)
    else:
        cprint("In %s year and %s days, you will die. " %
               (p.get_date_till_death()[0], p.get_date_till_death()[1]), t)


def smartinput(prompt, dtype):
    ans = input(prompt)
    if dtype is int:
        try:
            ans = int(raw_input(prompt))
        except ValueError:
            print "Numbers only!"
    else:
        ans = raw_input(prompt)

    return ans

# smartinput('test: ', int)

# ----------------------------------- Player control functions ---------------------------------------- #


def compact_dream_travel(world, days=1, do_dream=True, do_pause=True):
    if do_dream:
        dream(world, days)
    change_date(world, days)
    world.player.age += days
    if world.player.should_die():
        player_die(world, of_age=True)
    if do_pause:
        brief_pause()
    return 0


def move_player(mapobj):
    direction = raw_input("Direction: ")
    magnitude = input("For how long?: ")
    d_pos = cardinal_to_dp(direction.lower(), float(magnitude))
    mapobj.player.change_position(d_pos[0], d_pos[1])
    sleep(0.5)
    cprint("Moving %s . . ." % (direction.upper()))
    compact_dream_travel(world=mapobj, days=int(magnitude))
    return 0


def report_ship_status(mapobj):
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
        # distance = evaluate_distance(obj[1], vision)
        distance = obj[1]
        direction = obj[2]
        if distance == 0:
            cprint(string=("\t%s. Located on current grid." % count), t=0.011)
        elif (distance / float(vision)) > 80:
            cprint(string=("\t%s. %s days away: %s(?)" % (count, str(distance)[0:4], direction)), t=0.011)
        else:
            cprint(string=("\t%s. %s days away: %s" % (count, str(distance)[0:4], direction)), t=0.011)
        count += 1

    brief_pause()
    return 0


def investigate_space_menu(surroundings, vision, mapobj):
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
        cprint(string=("\t%s. %s: %s" % (count, distance, direction)), t=0.012)
        count += 1

    print(make_border())

    ans = raw_input()

    ans_obj = surroundings[int(ans) - 1]
    distance_obj = ans_obj[1]
    obj_select = ans_obj[0]

    investigate_space_details(mapobj, obj_select, distance_obj)

    compact_dream_travel(mapobj)

    return 0


def investigate_space_details(mapobj, obj, distance):
    if distance == 0:
        sleep(0.5)
        print make_border()
        cprint(string=obj.inspect_detailed(), t=0.03)
        mapobj.player.encounters.append(obj)
        print make_border()

        approach_scene_dialogue(mapobj, obj)

    else:
        sleep(0.5)
        print make_border()
        cprint(string=obj.inspect_vague(), t=0.03)
        print make_border()


def report_personal_status(world):
    years_till_dead = world.player.get_date_till_death()
    cprint("You are currently %s years old. \nYou are %s.\nYour birthday is on September sixth."
            % (world.player.get_age_years(), world.player.height))
    if years_till_dead == 1:
        cprint("You will die in less than one year. ")
    else:
        cprint("In %s year(s) and %s day(s), you will die. " % (years_till_dead[0], years_till_dead[1]))
    world.egg_time.print_time_elapsed()
    if Artifact() in world.player.encounters:
        cprint("You feel an uneasy darkness settling in your blood. ")
    else:
        cprint("You feel hopeless. ")
    brief_pause()


def player_sleep(mapobj):
    cprint("How many days would you like to sleep for?: ", t=0.03)
    days = int(raw_input())
    cprint("Zzz . . . ", t=0.20)
    compact_dream_travel(world=mapobj, days=days)


def player_die(world, of_age=False):
    adj1 = ch(ch(adjectives_lists))
    adj2 = ch(ch(adjectives_lists))
    adj3 = ch(ch(adjectives_lists))
    if of_age:
        cprint("Your age has overcome you. \nYou keel over and die. ", t=0.15)
    else:
        cprint("You decided searching was too much. \nYou end your life. ", t=0.15)
    brief_pause()
    world.egg_time.print_time_elapsed()
    num_encounters = len(world.player.encounters)
    num_dreams = len(world.player.dreams)
    cprint(string="You had %s encounter(s) and %s dream(s)." % (num_encounters, num_dreams))
    cprint(string="You had %s birthday(s) in 'EGGSPACE'. " % world.egg_time.birthdays_had)
    cprint(string="You were %s years old. " % world.player.get_age_years())
    sleep(0.5)
    cprint(string="Your journey was . . . %s, %s, and %s. " % (adj1, adj2, adj3))
    brief_pause("Enter to exit . . . ")
    exit()

# ---------------------------------------------- Area visitations  ---------------------------------------- #


def is_landable(obj):
    if obj in [Wreckage(), Planet()]:
        return True


def approach_scene_dialogue(mapobj, obj):
    cprint("You grow curious. Do you go in for a closer look? [Y/N]: ")
    ans = raw_input()
    if ans.lower() == 'y':
        obj.scene.player = mapobj.player
        approach_scene_menu(obj)
    else:
        return 0


def approach_scene_menu(obj):
    if is_landable(obj):
        cprint("You have landed on %s. " % obj.name)
    else:
        cprint("You move in for a closer look at %s. " % obj.name)
    stay = True
    while stay:

        cprint('The surface temperature is a constant %sK. ' % obj.scene.temperature)
        cprint('The atmosphere is %s. '% obj.scene.atmosphere)
        cprint('You feel %s. ' % player_temp_reaction(obj.scene.temperature))

        cprint("Options:\n\ti - Investigate\n\tl - Leave", 0.01)
        ans = raw_input()

        if ans.lower() == 'i':
            investigate_scene_menu(obj)
        elif ans.lower() == 'l':
            cprint("You pack your things and leave. ")
            stay = False


def investigate_scene_menu(obj):
    ## TODO: Should print out a list of all rooms in the scene. Once room is selected, print out objects.
    ## TODO: Should print out special surface stats e.g. temperature as well
    scene = obj.scene
    rooms = obj.scene.rooms

    print_scene_info(scene)
    if rooms:
        cprint('Select room to enter: ')
        ans = raw_input()

        investigate_scene_room(rooms, ans)

    pass


def print_scene_info(scene):
    if scene.rooms:
        cprint('Your sensors indicate several points of interest: ')
        return scene.rooms.list_rooms()


def investigate_scene_room(rooms, ans):
    room = ans
    room_contents = rooms.introduce_room_contents(room)

    while 1 == 1:
        cprint('What object do you inspect? [E] to exit ')
        ans = raw_input()

        if ans.lower() == 'e': break
        cprint(rooms.get_obj_desc(room_contents, ans))
        brief_pause()
        rooms.list_room_contents(room)


def player_temp_reaction(temperature):
    reaction = None
    if 0 < temperature < 280:
        reaction = ch(adj_temperature_cold)
    else:
        reaction = ch(adj_atmosphere_hot)
    return reaction

# ----------------------------------- Navigation and movement functions ---------------------------------------- #


def evaluate_distance(distance, vision):
    ratio = distance / vision
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
        "n": (0, d_pos), "e": (d_pos, 0), "s": (0, -d_pos), "w": (-d_pos, 0),
        "ne": (d_pos, d_pos),
        "nw": (-d_pos, d_pos),
        "sw": (-d_pos, -d_pos),
        "se": (d_pos, -d_pos)
    }

    return card_coord[card]


def get_date(world):
    world.egg_time.print_date()
    return 0


def change_date(world, days=1):
    world.egg_time.change_date(days)


# -------------------------------------------- Player Status Functions --------------------------------------------- #


def dream(world, days=1, dream_chance=5):
    roll = randint(0, 100)
    if days == 2.713:
        dream_chance *= log(days)
    else:
        dream_chance += days

    dream_list = [dreams_normal]

    if roll < dream_chance:
        if Artifact() in world.player.encounters:
            dream_list.append(dreams_terror)
        elif Wreckage() in world.player.encounters:
            dream_list.append(dreams_wreckage)

        # print dream_list

        dream_string = world.player.dream(ch(dream_list))
        cprint('You have a dream . . . ', t=0.10)
        cprint(dream_string)

    return 0

# c = WreckageRooms()

# investigate_scene_room(c, 'control room')