# Orbit.py
"""
    Creates object of type Orbit with the following attributes:
    position (0-14)
    distance (in AU)
    zone (Vaporization, Inner, Habitable, Outer)
    obj (Planet, GasGiant, Asteroids, None)
"""

distances = ['0.2', '0.4', '0.7', '1.0', '1.6', '2.8', '5.2', '10.0', '19.6',
             '38.8', '77.2', '154.0', '307.4', '614.8', '1129.2', '2458.0']


class Orbit:
    def __init__(self, position, distance, zone):
        self.position = position
        self.distance = distance
        self.zone = zone
        self.obj = []

    def add_object(self, obj):
        self.obj.append(obj)

