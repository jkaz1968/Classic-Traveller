# Star.py
"""
    Creates object of type Star with the following attributes:
    name (as entered)
    color (OBAFGKM)
    dec (0-9)
    size (Ib - VI, D, SD) - from super giants to dwarf stars
    min_orbit - the innermost orbit available
    max_orbit - the furthest orbit available
    hab_orbit - the habitable zone orbit, if available
    orbits - an array containing objects of type Orbit
"""


class Star:
    def __init__(self, name, color, size, min_orbit, max_orbit, hab_orbit, orbits):
        self.name = name
        self.color = color
        self.size = size
        self.min_orbit = min_orbit
        self.max_orbit = max_orbit
        self.hab_orbit = hab_orbit
        self.orbits = []

    def add_orbit(self, orbit):
        self.orbits.append(orbit)

