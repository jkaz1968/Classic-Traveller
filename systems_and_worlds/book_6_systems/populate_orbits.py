# populate_orbits.py
# creates an array of Orbit objects populated by Planet objects
# which can be Planets, Gas Giants, or Asteroid Belts

import random
import Orbit
import Planet


def roll_two_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def create_the_orbits(star):
    empty_orbits = []
    for orbit in range(star.min_orbit, star.max_orbit):
        orb = Orbit.Orbit(orbit, Orbit.distance[orbit], star.orbits[orbit], None)
        empty_orbits.append(orb)
    for x in empty_orbits:
        print("{}  {}  {}  {}".format(x.position, x.distance, x.zone, x.object))
    return empty_orbits


def place_gas_giants(star, pop_orbits):
    roll = roll_two_dice()
    gas_qty = 0
    if roll < 10:
        roll2 = roll_two_dice()
        if roll2 <= 3:
            gas_qty = 1
        elif roll2 <= 5:
            gas_qty = 2
        elif roll2 <= 7:
            gas_qty = 3
        elif roll2 <= 10:
            gas_qty = 4
        else:
            gas_qty = 5
    if gas_qty > 0:
        for a in range(1, gas_qty):
            selected_orbit = random.randint(star.min_orbit, star.max_orbit)
            if star.orbits[selected_orbit]:
                break
        a = 0
    return pop_orbits


def place_planetoid_belts(star, pop_orbits):
    return pop_orbits


def create(star):
    populated_orbits = []  # a list containing orbit objects that will become populated with Planet objects
    star.orbits = create_the_orbits(star)
    place_gas_giants(star, populated_orbits)
    place_planetoid_belts(star, populated_orbits)

    return populated_orbits
