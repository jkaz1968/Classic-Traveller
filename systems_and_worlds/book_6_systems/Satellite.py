# Satellite.py
"""
    Creates object of type Satellite with the following attributes:
    distance (in diameters)
    type (Ring, Moon)
    upp (the upp of the world, if applicable; None if Ring)
"""


class Satellite:
    def __init__(self, distance, kind, upp):
        self.distance = distance
        self.kind = kind
        self.upp = upp

