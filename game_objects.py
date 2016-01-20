from dialogue.dialogues import *
from dialogue.scene_dialogues import WreckageRooms
from printer import cprint
from datetime import datetime, timedelta

# ------------------------------------------------- Player Object --------------------------------------------------- #


class Player(object):
    def __init__(self, name, health, encounters=None, position=None, vision=100):
        self.name = name
        self.health = health
        self.encounters = encounters
        self.position = position
        self.vision = vision
        self.height = "5'9"
        self.age = randint(22500, 23000)  # in days
        self.age_death = randint(23500, 23600)
        self.dreams = []

    def get_position(self):
        return self.position

    def get_age_years(self):
        return self.age / 365

    def get_date_till_death(self):
        days_raw = self.age_death - self.age
        years = days_raw / 365
        days = days_raw % 365
        return years, days

    def change_position(self, dx, dy):
        return self.position.d_pos(dx, dy)

    def dream(self, dream_dic):
        dream_string = generate_dialogue((dream_dic,))
        self.dreams.append(dream_string)
        return dream_string

    def should_die(self):
        if self.age >= self.age_death:
            return True
        else:
            return False

    def get_surroundings(self, vision, objects):
        """
        :param vision: Integer representing the maximum distance to which the player may "see"
        :param objects: Dictionary containing objects and their coordinates. Given by Map.get_objects.
        :return: Returns a tuple containing tuples with the name of the object, distance from the object, and the
        cardinality relative to the position of the player.
        """
        in_range = ()
        pos = self.position
        for e in objects.keys():
            d = pos.distance(e)
            if d <= vision:
                in_range += ((objects[e], d, pos.cardinality(e)),)

        return in_range

    def __str__(self):
        vals = [self.name, self.health, self.encounters, self.position]
        stringrep = ""
        for e in vals:
            stringrep += str(e) + ", "

        return stringrep[:-2]

    def __repr__(self):
        return str((self.x, self.y))


# ------------------------------------------------- Time Object ----------------------------------------------------- #


class EggTime(object):
    def __init__(self):
        self.year = randint(2390, 2410)
        self.month = randint(1, 12)
        self.day = randint(1, 31)
        self.date = datetime(self.year, self.month, self.day, now.hour, now.minute)

        self.time_elapsed = 0
        self.birthday = (6, 9)  # Day: month
        self.birthdays_had = 0
        self.christmas = (25, 12)

    # def __init__(self):
    #     self.year = randint(2390, 2410)
    #     self.month = randint(1, 12)
    #     self.day = randint(1, 31)
    #     self.time_elapsed = 0
    #     self.birthday = (6, 9)  # Day: month
    #     self.birthdays_had = 0
    #     self.christmas = (25, 12)

    def change_date(self, days):
        if days > 1:
            cprint("%s days have passed." % days)
        else:
            cprint("One day has passed.")

        self.date.timedelta(days=days)

    # def change_date(self, days):
    #     day_init = self.day
    #     month_init = self.month
    #     year_init = self.year
    #
    #     if days > 1:
    #         cprint("%s days have passed." % days)
    #     else:
    #         cprint("One day has passed.")
    #
    #     self.day += days
    #     self.time_elapsed += days
    #
    #     while self.day > 31:
    #         self.day -= 31
    #         self.month += 1
    #
    #     while self.month > 12:
    #         self.month -= 12
    #         self.year += 1
    #
    #     self.holidays_passed(day_init, self.day, month_init, self.month, year_init, self.year)
    #
    #     return 0
    #
    # def holidays_passed(self, day_i, day_f, month_i, month_f, year_i, year_f):
    #     had_birthday = self.check_holiday(day_i, day_f, month_i, month_f, year_i, year_f, self.birthday)
    #     had_christmas = self.check_holiday(day_i, day_f, month_i, month_f, year_i, year_f, self.christmas)
    #
    #     if had_birthday:
    #         cprint('Your birthday has passed. ', 0.15)
    #         self.birthdays_had += 1
    #
    #     if had_christmas:
    #         cprint('Christmas has passed. ', 0.15)
    #
    # @staticmethod
    # def check_holiday(day_i, day_f, month_i, month_f, year_i, year_f, holiday):
    #     """I am so sorry for whoever has to go back and try to understand this code
    #     Also: it doesn't actually work sometimes so idk"""
    #     had_holiday = False
    #     d_years = year_f - year_i
    #     days_holiday = holiday[0] + (holiday[1] * 31)
    #     days_init = day_i + (month_i * 31)
    #     days_final = day_f + (month_f * 31) + (d_years * 403)
    #
    #     if days_final < days_init:  # In case the year cycles, so we can still compare dates near end of the year
    #         days_final += 403
    #
    #     # print days_holiday, days_init, days_final
    #
    #     if days_init <= days_holiday <= days_final:
    #         had_holiday = True
    #
    #     return had_holiday
    #
    # def print_date(self):
    #     cprint('It is currently the year %s, day %s of month %s.' % (self.year, self.day, self.month), 0.02)
    #     return 0
    #
    # def print_time_elapsed(self):
    #     elapsed = days_to_date(self.time_elapsed)
    #     years = elapsed[0]
    #     months = elapsed[1]
    #     days = elapsed[2]
    #     cprint('It has been %s year(s), %s month(s), and %s day(s) since you began your search. '
    #            % (years, months, days))
    #     return 0
    #
    # def __repr__(self):
    #     return 'Year %s, day %s of month %s.' % (self.year, self.day, self.month)

# e = EggTime()
# e.print_date()
# for x in xrange(20):
#     e.change_date(30)
#     e.print_date()

# ------------------------------------------------- Space Objects --------------------------------------------------- #


class SpaceObject(object):
    def __init__(self, name=None, scene=None):
        self.name = self.generate_name()
        self.header = self.generate_header()
        self.desc_vague = self.generate_desc_vague()
        self.desc_detailed = self.generate_desc_detailed()
        self.footer = self.generate_footer()
        self.scene = scene

    def inspect_vague(self):
        cprint(string=("OBJ-ID: " + self.name), t=0.12)
        cprint(string='. . . . . ', t=0.30)
        sleep(0.2)
        return self.header + '\n' + self.desc_vague

    def inspect_detailed(self):
        cprint(string=("ID: " + self.name), t=0.12)
        cprint(string='. . . . . ', t=0.30)
        sleep(0.2)
        return self.header + '\n' + self.desc_detailed + '\n' + self.footer

    def generate_name(self):
        raise NotImplementedError

    def generate_header(self):
        raise NotImplementedError

    def generate_desc_vague(self):
        raise NotImplementedError

    def generate_desc_detailed(self):
        raise NotImplementedError

    def generate_footer(self):
        raise NotImplementedError

    def get_name(self):
        return self.name

    def get_desc_vague(self):
        return self.desc_vague

    def get_desc_detailed(self):
        return self.desc_detailed

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return type(self) == type(other)


class Artifact(SpaceObject):
    def __init__(self, name="Artifact"):
        super(Artifact, self).__init__(name=name, scene=ArtifactScene())

    def generate_name(self):
        return generate_name(4, 2)

    def generate_header(self):
        return generate_dialogue((desc_artifact_header,))

    def generate_desc_vague(self):
        return generate_dialogue((desc_artifact_vague,))

    def generate_desc_detailed(self):
        return generate_dialogue((desc_artifact_detailed,))

    def generate_footer(self):
        return generate_dialogue((desc_artifact_footer,))


class Wreckage(SpaceObject):  # TODO: Make specific wreckage types have correlated Scene() and descriptions.
    def __init__(self, name="Wreckage"):
        super(Wreckage, self).__init__(name=name, scene=WreckageScene())

    def generate_name(self):
        return generate_name(4, 4)

    def generate_header(self):
        return generate_dialogue((desc_wreckage_header,))

    def generate_desc_vague(self):
        return generate_dialogue((desc_wreckage_vague,))

    def generate_desc_detailed(self):
        return generate_dialogue((desc_wreckage_detailed,))

    def generate_footer(self):
        return generate_dialogue((desc_wreckage_footer,))


class Planet(SpaceObject):
    def __init__(self, name="Planet"):
        super(Planet, self).__init__(name=name, scene=PlanetScene())

    def generate_name(self):
        return generate_name_astral_body(name_list)

    def generate_header(self):
        return generate_dialogue((desc_planet_header,))

    def generate_desc_vague(self):
        return generate_dialogue((desc_planet_vague,))

    def generate_desc_detailed(self):
        return generate_dialogue((desc_planet_detailed,))

    def generate_footer(self):
        return generate_dialogue((desc_planet_footer,))


class Star(SpaceObject):
    def __init__(self, name="Star"):
        super(Star, self).__init__(name=name, scene=StarScene())

    def generate_header(self):
        return generate_dialogue((desc_star_header,))

    def generate_name(self):
        return generate_name_astral_body(name_list)

    def generate_desc_vague(self):
        return generate_dialogue((desc_star_vague,))

    def generate_desc_detailed(self):
        return generate_dialogue((desc_star_detailed,))

    def generate_footer(self):
        return generate_dialogue((desc_star_footer,))


# ------------------------------------------------- Scene Objects --------------------------------------------------- #

class Scene(object):
    def __init__(self, name=None, player=None, temperature=None, rooms=None, atmosphere=None):
        self.name = name
        self.player = player
        self.rooms = rooms
        self.temperature = temperature
        self.atmosphere = atmosphere

    def __repr__(self):
        return self.player.name


class WreckageScene(Scene):
    def __init__(self):
        super(WreckageScene, self).__init__(
            name='WreckageScene',
            temperature=randint(15, 42),
            rooms=WreckageRooms(),
            atmosphere=ch(adj_atmosphere_bad)
        )


class PlanetScene(Scene):
    def __init__(self):
        super(PlanetScene, self).__init__(
            name='PlanetScene',
            temperature=ch([randint(15, 42), randint(500, 800)]),
            atmosphere=ch(ch([adj_atmosphere_bad, adj_atmosphere_good]))
        )


class ArtifactScene(Scene):
    def __init__(self):
        super(ArtifactScene, self).__init__(
            name='ArtifactScene',
            temperature=ch([randint(2, 6), randint(2400, 3000)]),
            atmosphere=ch(adj_atmosphere_bad)
        )


class StarScene(Scene):
    def __init__(self):
        super(StarScene, self).__init__(
            name='StarScene',
            temperature=randint(3000, 30000),
            atmosphere=ch(adj_atmosphere_hot)
        )



