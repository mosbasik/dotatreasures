#!/usr/bin/python

import json
import pprint

# load the data files into dictionaries
heroes = json.load(open('heroes.json', 'r'))
treasures = json.load(open('treasures.json', 'r'))

# find out which heroes are represented in the treasures
heroes_with_treasures = set()
for treasure in treasures:
    for hero in treasures[treasure]:
        heroes_with_treasures.add(hero)

# filter the heroes dictionary to only include relevant heroes
heroes = {x: heroes[x] for x in heroes if x in heroes_with_treasures}

# initialize scoring dictionary
treasure_score = {x: 0 for x in treasures}

# get a value for each set by multiplying the set rating and hero rating together
# get a value for each treasure by summing the values of its sets
# store these values in the scoring dictionary
for treasure in treasure_score:
    for hero in treasures[treasure]:
        treasure_score[treasure] += int(treasures[treasure][hero]) * int(heroes[hero])

# make a list out of the scoring dictionary
score = [(treasure_score[x], x) for x in treasure_score]

# sort it by value
score.sort(key=lambda tup: tup[0], reverse=True)

# print the result
pprint.pprint(score)