# Planet.py
"""
    Creates object of type Planet with the following attributes:
    name (as entered)
    upp (the upp of the world, if applicable)
    satellites (an array of satellite objects)
"""


class Planet:
    def __init__(self, name, upp):
        self.name = name
        self.upp = upp
        self.satellites = []

    def add_satellite(self, satellite):
        self.satellites.append(satellite)


