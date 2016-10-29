# system_generator.py
# book 6 - Scouts
# enhanced star system generation

# program modules
import create_star
import populate_orbits


def intro():
    return


def main():
    star = create_star.create()
    print("{} {} {} \nOrbits: {}\nMinimum Available Orbit: {}"
          "\nHabitable Orbit: {}\nMaximum Available Orbit: {}".format(star.name, star.color, star.size,
                                                                      star.orbits, star.min_orbit, star.hab_orbit,
                                                                      star.max_orbit))
    star.orbits = populate_orbits.create(star.orbits)


main()
