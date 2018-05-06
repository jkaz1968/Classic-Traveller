# aslan.py - word generator to create aslan language words

import random
import os, pathlib
import aslan_syllables


def roll_a_dice():
    return random.randint(1, 6)


def syllable(word, i):
    sequence = random.randint(1, 36)
    if i == 0 or word[i-1] == 'CV' or word[i-1] == 'V':
        if sequence <= 13:
            return "V"
        elif 13 < sequence <= 24:
            return "CV"
        elif 24 < sequence <= 30:
            return "VC"
        else:
            return "CVC"
    else:
        if sequence <= 15:
            return "V"
        else:
            return "VC"


def word_pattern():
    word_length = roll_a_dice()
    word_pattern = []
    for i in range(word_length):
        word_pattern.append(syllable(word_pattern, i))
    return word_pattern


def make_word(pattern):
    word = ""
    for syllable in pattern:
        if syllable == "V":
            word += aslan_syllables.vowel[random.randint(0, 5)][random.randint(0, 5)][random.randint(0, 5)]
        if syllable == "CV":
            word += aslan_syllables.initial_consonant[random.randint(0, 5)][random.randint(0, 5)][random.randint(0, 5)]
            word += aslan_syllables.vowel[random.randint(0, 5)][random.randint(0, 5)][random.randint(0, 5)]
        if syllable == "VC":
            word += aslan_syllables.vowel[random.randint(0, 5)][random.randint(0, 5)][random.randint(0, 5)]
            word += aslan_syllables.final_consonant[random.randint(0, 5)][random.randint(0, 5)][random.randint(0, 5)]
        if syllable == "CVC":
            word += aslan_syllables.initial_consonant[random.randint(0, 5)][random.randint(0, 5)][random.randint(0, 5)]
            word += aslan_syllables.vowel[random.randint(0, 5)][random.randint(0, 5)][random.randint(0, 5)]
            word += aslan_syllables.final_consonant[random.randint(0, 5)][random.randint(0, 5)][random.randint(0, 5)]
    return word


def main():
    number_of_words = int(input("How many words to make? "))
    path = "Words"
    directory = os.path.dirname(__file__)
    pathlib.Path(path).mkdir(exist_ok=True)
    name = "Words"
    filename = os.path.join(directory, path, name)
    f = open(filename + ".txt", "w")

    for w in range(number_of_words):
        pattern = word_pattern()
        word = make_word(pattern)
        # print(pattern)
        f.write(word + '\n')
    print("List written to {}.txt".format(name))

        # print(make_word(pattern))


main()