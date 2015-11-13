from random import choice as ch
from time import sleep
from os import system, name


# -------------------------------------- Dialogue Selectors / Generators ------------------------------------------- #


def random_dialogue(l):
    return ch(l)


def cls():
    system('cls' if name == 'nt' else 'clear')


def brief_pause(string="Enter to continue . . . "):
    raw_input(string)
    return 0


def make_border(length=50):
    return "-" * length


def days_to_date(days):
    count_years = 0
    count_months = 0
    for i in xrange(100):
        if days < 365:
            break
        days -= 365
        count_years += 1

    for i in xrange(100):
        if days < 31:
            break
        days -= 31
        count_months += 1
    return count_years, count_months, days


def generate_name(letters=5, numbers=3):
    gen = ''
    letterl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numberl = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for i in xrange(letters):
        gen += (ch(letterl).upper())
    gen += '-'
    for j in xrange(numbers):
        gen += (ch(numberl))
    return str(gen)


def generate_dialogue(dialogue_tup):
    gen = ''
    adjs = ()

    for entry in dialogue_tup:
        dialogue = ch(entry.keys())
        for e in entry[dialogue]:
            adjs += (ch(e),)
        if adjs == '':
            gen += dialogue
        else:
            gen += (dialogue % adjs)

    return gen


# -------------------------------------------- Adjective Banks --------------------------------------------------- #


investigate_space = [
    "You check the sensors. Nothing within a waking day's reach . . .",
    "You head to the deck. A faint glimmer in the distance, but nothing more . . . ",
    "The cameras outside the ship buzz and whir. Only starlight and the vacuum . . . ",
    "The shielding lifts from the glass. You observe shimmering lights and unchanging blackness . . . ",
    "You stare out into the darkness. You spot something in the dim, but quickly dismiss it . . . ",
    "You rest your head against the wall. The ship trembles as a heat sink is ejected and replaced with vacuum outside . . . "
]

adj_large = [
    'extensive', 'immense', 'cavernous', 'vast', 'boundless', 'colossal', 'enormous', 'great', 'infinite', 'limitless',
    'mammoth', 'tremendous', 'capacious', 'gigantic', 'behemoth', 'cyclopean', 'elephantine', 'gross', 'immeasurable',
    'titanic', 'mountainous', 'leviathan', 'towering', 'perpetual', 'unending', 'inexhaustible', 'incalculable'
]

adj_pos = [
    'grand', 'opulent', 'imposing', 'glittering', 'shimmering', 'sublime', 'palatial', 'elegant', 'gorgeous', 'stately',
    'exalted', 'transcendent', 'heavenly', 'illustrious', 'dazzling', 'lovely', 'magnificent', 'exquisite', 'fine',
    'striking', 'angelic', 'radiant', 'beauteous', 'ethereal', 'divine'
]

adj_neg = [
    'blemished', 'sullied', 'debased', 'tainted', 'tarnished', 'blackened', 'tarred', 'besmirched', 'defiled',
    'discolored', 'faded', 'desecrated', 'degraded', 'vitriolic', 'grisly', 'hideous', 'horrid', 'revolting',
    'misshapen', 'deformed', 'disfigured', 'foul', 'distorted', 'mutilated'
]

adj_strange = [
    'astonishing', 'bizarre', 'extraordinary', 'peculiar', 'rare', 'remarkable', 'unusual', 'grotesque', 'ludicrous',
    'outlandish', 'alien', 'eerie', 'monstrous', 'surreal', 'strange', 'atrocious', 'dreadful', 'frightful',
    'gruesome', 'inhuman', 'obscene', 'hideous', 'odious'
]

adjectives_planet_type = [
    # TODO
]

adjectives_lists = [
    adj_large, adj_pos, adj_neg, adj_strange
]

# -------------------------------------------- Description Banks --------------------------------------------------- #


desc_artifact_header = {
    "A cabalistic anomaly . . . ": '',
    "Esoteric in nature and insatiable in its abnormality . . . ": '',
    "Formless, yet lovingly shaped . . . ": ''
}

desc_artifact_detailed = {
    "You approach the object. Your ship reaches out to it. "
    "Upon closer inspection you see that it is detailed with %s scripture, incomprehensible, yet "
    "%s in its scrawl. It spews %s amounts of radiation and heat from the %s cracks that line its surface. "
    "Although its initial signature seemed %s, you are surprised to find that it is no larger than a small child. ":
        (adj_strange, adj_pos, adj_large, adj_neg, adj_large),
    "You have arrived. The ship searches for the %s anomaly but instead find a shapeless and %s mass, no larger than a small "
    "child. It rotates furiously, emitting %s beams of light as it spins. From time to time, the object "
    "suddenly pivots about an axis, dancing in a graceful, but %s manner. You are terrified to find that your sensors indicate that "
    "the object is emitting sound waves in what should be a total vacuum. ":
        (adj_large, adj_strange, adj_pos, adj_strange),
    "You approach the object. "
    "Your hands sweat profusely and your heart races wildly without reason. Your ship's "
    "lights illuminate the object's surface, revealing the %s and %s warts that encrust it entirely. Each blemish "
    "undulates rhythmically, emitting %s trails of heat and radiation with every fluctuation. Although the object "
    "is no larger than a baby's crib, all the space behind it is a thick and %s blackness. ":
        (adj_large, adj_neg, adj_pos, adj_strange),
    "You approach the object. "
    "Your ship tries its best to align its lights and sensors on the object, but struggles. After waiting for "
    "several hours, you realize why. The object is a perfect sphere, shaped with %s and %s precision. "
    "In its reflection you spot something %s. Its %s figure speaks of some %s nature and %s intent. "
    "The very thought of it fills you with %s dread. "
    "The sphere's %s surface constantly rises and falls, as if the stomach of a sleeping child. ":
        (adj_pos, adj_strange, adj_large, adj_strange, adj_neg, adj_strange, adj_pos, adj_pos),
    "Your ship closes the distance between itself and the object. The lights inside the cabin flicker rhythmically. "
    "The ship illuminates the object and reveals a familiar, yet %s sight. It is an escape pod from a well-known "
    "line of mining ships. There is room for a single occupant. You align the %s signals you detected earlier with "
    "the distress signals being emitted from the pod. You note something %s. "
    "The exhaust ports of the pod's life support system are dotted with %s streams of an unknown liquid. "
    "Your ship detects %s amounts of radiation being emitted from the center of the pod. "
    "The pods are designed to support its users for up to two weeks. The %s signal indicates its age to be more "
    "than two centuries old. ":
        (adj_strange, adj_strange, adj_strange, adj_large, adj_large, adj_pos)
}

desc_artifact_footer = {
    "A dark wind pours from its core. ": '',
    "A warm, deep hum fills the ship. ": '',
    "A strange cacophony of sounds rings in your ears. ": '',
    "You think of home. ": ''
}

desc_artifact_vague = {
    "It emits a %s hum and is trailed by an ionic residue that is %s in size. "
    "The thought of coming closer to it brings to mind both things %s and %s. ":
        (adj_pos, adj_large, adj_pos, adj_neg),
    "A %s presence where there should be none. You recalibrate your sensors and try again. "
    "A %s dread washes over you as it reappears on the screen, %s and %s.":
        (adj_neg, adj_neg, adj_large, adj_pos)
}

# -------------------------------------------- Dreams -------------------------------------------------------- #

dreams_normal = {
    "You are home . . . It is the year 2342. You see your reflection in a passing mirror and you are whole. "
    "You step into the living room and greet your family. You laugh. There is no emptiness. Every pore in your skin is "
    "overflowing with love. ":
        '',
    "The sun is setting. You are on a cliff. You are holding the hand of the one you love. Her face is %s. She laughs. "
    "It echoes in the valley.":
        (adj_pos),
    "You are on a beach. The water is %s. You are an arm's length from the one you love. "
    "A %s wind falls from the crashing waves and chills you to the bone. She comes near and it leaves. ":
        (adj_pos, adj_neg)
}

dreams_terror = {
    "You are home . . . It is the year 2342. Your home is suspended in a grotesque and %s emptiness. "
    "It is preparing for its journey. You meet your crew. Their faces are %s. You shake their hands. "
    "Their flesh melds into yours and you become a single flesh-ridden mass. The air around you turns %s.":
        (adj_large, adj_neg, adj_strange),
    "The beach is on fire. The flames are %s in size. The hand of the one you love melts into yours. Your flesh "
    "becomes candle wax and your bones become the wick. You burn with a flame powerful and %s. ":
        (adj_large, adj_pos),
    "You are next to the object. It spins and changes shape constantly. Its surface is covered with %s script. "
    "You read them and realize they are your thoughts. They object shrinks into nothingness. A void, %s and %s, "
    "is all that remains.":
        (adj_pos, adj_large, adj_strange)
}

# print generate_dialogue((dreams_terror,))
# print generate_dialogue((dreams_normal,))
#


# print generate_name()
