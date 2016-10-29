# create_star.py
# module used to generate an empty star system

import random

import Star
import startypes


def roll_two_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def get_star_color():
    roll = roll_two_dice()
    color = ''
    if roll <= 2:
        color += 'A'
    elif 2 < roll <= 7:
        color += 'M'
    elif roll == 8:
        color += 'K'
    elif roll == 9:
        color += 'G'
    else:
        color += 'F'
    print("get_star_color(): {}".format(color))
    # decimal classification step
    r2 = random.randint(0, 9)
    print("get_star_color(): {}".format(r2))
    if r2 < 5:
        color += '0'
    elif 5 <= r2 < 9:
        color += '5'
    elif r2 == 9:
        if color == 'M':
            color += '9'
        else:
            color += '5'

    # print("get_star_color(): {}".format(color))
    return color


def get_star_size(color):
    # print("get_star_size({})".format(color))
    roll = roll_two_dice()
    size = ''
    if roll == 2:
        size = 'Size II'
    elif roll == 3:
        size = 'Size III'
    elif roll == 4:
        if color == 'K5' or color[0] == 'M':
            size = 'Size V'
        else:
            size = 'Size IV'
    elif 4 < roll <= 10:
        size = 'Size V'
    elif roll == 11:
        size = 'Size VI'
    else:
        size = 'Dwarf'
    return size


def get_orbits(size, stype):
    # print("get_orbits({}, {})".format(size, stype))
    orbs = roll_two_dice()
    if size == 'Size III':
        orbs += 4
    if size == 'Size II':
        orbs += 8
    if stype == 'M':
        orbs -= 4
    if stype == 'K':
        orbs -= 2
    # print("get_orbits(): {}".format(orbs))
    return orbs


def get_stellar_orbits(size, color):
    # print("get_stellar_orbits({}, {})".format(size, color))
    if size == 'Dwarf':
        orbits = get_all_orbits(size, startypes.dwarf_colors.index(color))
    else:
        orbits = get_all_orbits(size, startypes.star_colors.index(color))
    return orbits


def get_all_orbits(size, color):
    # print("get_all_orbits({}, {})".format(size, color))
    orbits = []
    block = startypes.star_orbits[startypes.star_sizes.index(size)]
    for r in range(0, len(block)):
        orbits.append(block[r][color])
    # print("get_all_orbits(): {}".format(orbits))
    return orbits


def get_max_orbits(size, color):
    orbits = roll_two_dice()
    # print("get_max_orbits(): size {}  color {}".format(size, color))
    if size == 'Size III':
        orbits += 4
    if size == 'Size Ia' or size == 'Size Ib' or size == 'Size II':
        orbits += 8
    if color[0] == 'M':
        orbits -= 4
    if color[0] == 'K':
        orbits -= 2
    if orbits < 0:
        orbits = 0
    return orbits


def get_min_orbit(orbits):
    orbit = 0
    for orb in orbits:
        if orb == 'I' or orb == 'H' or orb == 'O':
            orbit = orbits.index(orb)
            break
    return orbit


def get_hab_orbit(orbits):
    orbit = None
    for orb in orbits:
        if orb == 'H':
            orbit = orbits.index(orb)
            break
    return orbit


def create():
    # star(name, color, size, min_orbit, max_orbit, hab_orbit, orbits)
    star = Star.Star("Alhazred", None, None, None, None, None, None)
    star.color = get_star_color()
    star.size = get_star_size(star.color)
    if star.size == 'Dwarf':
        star.color = 'D' + star.color[0]
        print(star.color)
    star.orbits = get_stellar_orbits(star.size, star.color)
    star.max_orbit = get_max_orbits(star.size, star.color)
    if star.max_orbit >= len(star.orbits):
        star.max_orbit = len(star.orbits)
    star.orbits = star.orbits[:star.max_orbit]
    star.min_orbit = get_min_orbit(star.orbits)
    star.hab_orbit = get_hab_orbit(star.orbits)
    # print("{} {} {} \nOrbits: {}\nMinimum: {}\nHabitable: {}\nMaximum: {}".format(star.name, star.color, star.size,
    #                                                                             star.orbits, star.min_orbit, star.hab_orbit,
    #                                                                              star.max_orbit))
    return star
