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


def generate_name(letters=5, numbers=3):
    name = ''
    letterl = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numberl = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for i in xrange(letters):
        name += (ch(letterl).upper())
    for j in xrange(numbers):
        name += (ch(numberl))
    return str(name)



def generate_dialogue(dialogue_tup):
    gen = ''

    for entry in dialogue_tup:
        dialogue = ch(entry.keys())
        adjs = entry[dialogue]
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
    #TODO
]

adjectives_lists = [
    adj_large, adj_pos, adj_neg
]

# -------------------------------------------- Description Banks --------------------------------------------------- #


desc_artifact_name = {

}


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
        (ch(adj_strange), ch(adj_pos), ch(adj_large), ch(adj_neg), ch(adj_large)),
    "You have arrived. The ship searches for the %s anomaly but instead find a shapeless and %s mass, no larger than a small "
    "child. It rotates furiously, emitting %s beams of light as it spins. From time to time, the object "
    "suddenly pivots about an axis, dancing in a %s manner. You are terrified to find that your sensors indicate that "
    "the object is emitting sound waves in what should be a total vacuum. ":
        (ch(adj_large), ch(adj_strange), ch(adj_pos), ch(adj_strange)),
    "You approach the object. "
    "Your hands sweat profusely and your heart races wildly without reason. Your ship's "
    "lights illuminate the object's surface, revealing the %s and %s warts that encrust it entirely. Each blemish "
    "undulates rhythmically, emitting %s trails of heat and radiation with each fluctuation. Although the object "
    "is no larger than a baby's crib, all the space behind it is a thick and %s blackness. ":
        (ch(adj_large), ch(adj_neg), ch(adj_pos), ch(adj_strange)),
    "You approach the object. "
    "Your ship tries its best to align its lights and sensors on the object, but struggles. After waiting for "
    "several hours, you realize why. The object is a perfect sphere, shaped with %s and %s precision. "
    "In its reflection you spot something %s. Its %s figure speaks of some %s nature and %s intent. "
    "The very thought of it fills you with %s dread. "
    "The sphere's %s surface constantly rises and falls, as if the stomach of a sleeping child. ":
        (ch(adj_pos), ch(adj_strange), ch(adj_large), ch(adj_strange), ch(adj_neg), ch(adj_pos), ch(adj_strange), ch(adj_pos)),
    "Your ship closes the distance between itself and the object. The lights inside the cabin flicker rhythmically. "
    "The ship illuminates the object and reveals a familiar, yet %s sight. It is an escape pod from a well-known "
    "line of mining ships. There is room for a single occupant. You align the %s signals you detected earlier with "
    "the distress signals being emitted from the pod. You note something %s. "
    "The exhaust ports of the pod's life support system are dotted with %s streams of an unknown liquid. "
    "Your ship detects %s amounts of radiation being emitted from the center of the pod. "
    "The pods are designed to support its users for up to two weeks. The distress signal indicates its age to be more "
    "than two centuries old. ":
        (ch(adj_strange), ch(adj_strange), ch(adj_strange), ch(adj_large), ch(adj_large))
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
        (ch(adj_pos), ch(adj_large), ch(adj_pos), ch(adj_neg)),
    "A %s presence where there should be none. You recalibrate your sensors and try again. "
    "A %s dread washes over you as it reappears on the screen, %s and %s.":
        (ch(adj_neg), ch(adj_neg), ch(adj_large), ch(adj_pos))
}

# print generate_dialogue((desc_artifact_header, desc_artifact_vague))
# print generate_dialogue((desc_artifact_header, desc_artifact_detailed, desc_artifact_footer))

# print generate_name()