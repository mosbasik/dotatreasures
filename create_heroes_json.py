#!/usr/bin/python

import json 

f = file('heroes.json', 'r')
try:
    foo = json.load(f)
    json_contents = foo
except ValueError:
    json_contents = dict()
f.close()

print 'Type \'q\' to [q]uit'
while True:

    hero = raw_input('Hero name: ')
    if hero == 'q':
        break
    else:
        hero_rating = raw_input('Hero rating [1-3]: ')
        json_contents[hero] = hero_rating


f = open('heroes.json', 'w')
json.dump(json_contents, f, indent=4)
f.close()