from random import choice as ch

# -------------------------------------- Dialogue Selectors / Generators ------------------------------------------- #


def random_dialogue(l):
    return ch(l)


def make_border(length=50):
    return "-" * length


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
    "You check the sensors. Nothing within a sol's reach . . .",
    "You head to the deck. A faint glimmer in the distance, but nothing more . . . ",
    "The cameras outside the ship buzz and whir. Only starlight and the vacuum . . . ",
    "The shielding lifts from the glass. You observe shimmering lights and unchanging blackness . . . ",
    "You stare out into the darkness. You spot something in the dim, but quickly dismiss it . . . ",
    "You rest your head against the wall. The ship trembles as a heat sink is ejected and replaced with vacuum outside . . . "
]

adj_large = [
    'extensive', 'immense', 'cavernous', 'vast', 'boundless', 'colossal', 'enormous', 'great', 'infinite', 'limitless',
    'mammoth', 'tremendous', 'capacious'
]

adj_pos = [
    'grand', 'opulent', 'imposing', 'glittering', 'shimmering', 'sublime', 'palatial', 'elegant', 'gorgeous', 'stately',
    'exalted', 'transcendent', 'heavenly', 'illustrious', 'dazzling', 'lovely', 'magnificent', 'exquisite', 'fine',
    'striking', 'angelic', 'radiant', 'beauteous', 'ethereal', 'divine'
]

adj_neg = [
    'blemished', 'sullied', 'debased', 'tainted', 'tarnished', 'blackened', 'tarred', 'besmirched', 'defiled',
    'discolored', 'faded', 'desecrated', 'degraded', 'vitriolic'
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


desc_artifact_header = {
    "A cabalistic anomaly . . . ": '',
    "Esoteric in nature and insatiable in its abnormality . . . ": '',
    "Formless, yet lovingly shaped . . . ": ''
}

desc_artifact_detailed = {
    "You approach the object. "
    "Upon closer inspection you see that it is detailed with %s scripture, incomprehensible yet "
    "%s in its scrawl. It spews %s amounts of radiation and heat from the %s cracks that line its surface. "
    "Although its initial signature seemed %s, you are surprised to find that it is no larger than a small child. ":
        (ch(adj_strange), ch(adj_pos), ch(adj_large), ch(adj_neg), ch(adj_large)),
    "You have arrived. You search for the %s anomaly but instead find a shapeless and %s mass, no larger than a small "
    "child. It rotates furiously, emitting %s beams of light as it whirls mindlessly. From time to time, the object "
    "suddenly pivots about an axis, dancing in a %s manner. You are terrified to find that your sensors indicate that "
    "the object is emitting sound waves in what should be a total vacuum. ":
        (ch(adj_large), ch(adj_strange), ch(adj_pos), ch(adj_strange))
}

desc_artifact_footer = {
    "A dark wind pours from its core. ": '',
    "A warm, deep hum fills the ship. ": '',
    "A strange and cacophonic sound rings in your ears. ": '',
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

#
# print generate_dialogue((desc_artifact_header, desc_artifact_vague))
#
# print generate_dialogue((desc_artifact_header, desc_artifact_detailed, desc_artifact_footer))