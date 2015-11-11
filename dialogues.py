from random import choice

# -------------------------------------- Dialogue Selectors / Generators ------------------------------------------- #


def random_dialogue(l):
    return choice(l)


def make_border(length=50):
    return ("-" * length)

# -------------------------------------------- Dialogue Banks --------------------------------------------------- #

investigate_space = [
    "You check the sensors. Nothing within a sol's reach . . .",
    "You head to the deck. A faint glimmer in the distance, but nothing more . . . ",
    "The cameras outside the ship buzz and whir. Only starlight and the vacuum . . . ",
    "The shielding lifts from the glass. You observe shimmering lights and unchanging blackness . . . ",
    "You stare out into the darkness. You spot something in the dim, but quickly dismiss it . . . ",
    "You rest your head against the wall. The ship trembles as a heat sink is ejected and replaced with vacuum outside . . . "
]

adjectives_large = [
    'extensive', 'immense', 'cavernous', 'vast', 'boundless', 'colossal', 'enormous', 'great', 'infinite', 'limitless',
    'mammoth', 'tremendous', 'capacious'
]

adjectives_pos = [
    'grand', 'opulent', 'imposing', 'glittering', 'shimmering', 'sublime', 'palatial', 'elegant', 'gorgeous', 'stately',
    'exalted', 'transcendent', 'heavenly', 'illustrious'
]

adjectives_neg = [
    'blemished', 'sullied', 'debased', 'tainted', 'tarnished', 'blackened', 'tarred', 'besmirched', 'defiled',
    'discolored', 'faded', 'desecrated', 'degraded', 'vitriolic'
]

adjectives_planet_type = [
    #TODO
]

