# characters.py
# random character generator for Classic Traveller

# character UPP: 777777
# Str, Dex, End, Int, Edu, Soc

import random

# career modules
import navy
import marines
import army
import scouts
import merchants
import belters
import pirates
import hunters
import nobles
import barbarian
import flyer

careers = ["Navy", "Marines", "Army", "Scouts", "Merchants", "Belters", "Pirates",
           "Hunters", "Nobles", "Barbarians", "Flyer"]


def roll_two_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def gen_upp():
    upp = []
    for stat in range(0, 6):
        upp.append(roll_two_dice())
    return upp


def start(name, upp):
    a = 0
    success = False
    count = 0
    print("Select a service to enlist in: ")
    for job in careers:
        print("{}. {}".format(a + 1, job))
        a += 1
    while success is False and count < 6:
        count += 1
        att = int(input("--> "))
        if att == 1:
            if navy.enlistment(upp):
                navy.career(name, 0, 18, 'Y', 'N', 0, upp)
        if att == 2:
            if marines.enlistment(upp):
                marines.career(name, 0, 18, 'Y', 'N', 0, upp)
        if att == 3:
            if army.enlistment(upp):
                army.career(name, 0, 18, 'Y', 'N', 0, upp)
        if att == 4:
            if scouts.enlistment(upp):
                scouts.career(name, 0, 18, 'Y', 0, upp)
        if att == 5:
            if merchants.enlistment(upp):
                merchants.career(name, 0, 18, 'Y', 'N', 0, upp)
        if att == 6:
            if belters.enlistment(upp):
                belters.career(name, 0, 18, 'Y', 0, upp)
        if att == 7:
            if pirates.enlistment(upp):
                pirates.career(name, 0, 18, 'Y', 'N', 0, upp)
        if att == 8:
            if hunters.enlistment(upp):
                hunters.career(name, 0, 18, 'Y', 0, upp)
        if att == 9:
            if nobles.enlistment(upp):
                nobles.career(name, 0, 18, 'Y', 'N', 0, upp)
        if att == 10:
            if barbarian.enlistment(upp):
                barbarian.career(name, 0, 18, 'Y', 'N', 0, upp)
        if att == 11:
            if flyer.enlistment(upp):
                flyer.career(name, 0, 18, 'Y', 'N', 0, upp)

def draft():
    return


def intro():
    print("""
Classic Traveller Character Creator

Generates random characters for the original Traveller game developed by Mark Miller in 1977.
Character stats were defined by a six-digit Universal Personality Profile or UPP, as explained:
Strength, Dexterity, Endurance, Intelligence, Education, Social Standing
Each stat is rated from 2 to 15 (2 to F in the final form) and initial values are generated by
rolling 2x six-sided dice.

Characters are presumed to be adults, typically on their own following a military or other
professional career, with nothing better to do than explore the galaxy and look for fame and
fortune.

We begin by giving the character a name and generating the UPP. You will then choose a career
path to follow.

    """)


def get_name():
    return input("What is your name? ")


def main():
    intro()
    name = get_name()
    upp = gen_upp()
    print("{}  UPP: {}".format(name, upp))
    start(name, upp)


main()