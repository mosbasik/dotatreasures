dotatreasures
=============

Small program to determine which Treasure to redeem given personal preferences
regarding hero use and cosmetic set quality.  Preference data is generated using
the `create_heroes_json.py` and `create_treasures_json.py` scripts and stored in
the two JSON files.  The answer is then computed by running `crunch.py`

Results on 3 Nov '14: 

    [(39, u'Treasure of the Rotted Gallows'),
     (28, u'Treasure of the Tangled Keepsake'),
     (27, u'Treasure of the Eternal Alliance'),
     (23, u"Treasure of the Summit's Peak"),
     (22, u"Treasure of the Mender's Palm"),
     (20, u'Treasure of the Forged Fury'),
     (18, u'Treasure of the Onyx Eye'),
     (16, u"Treasure of the Cannon's Fuse"),
     (13, u'Treasure of the Elemental Trophy'),
     (6, u'Treasure of the Fractured Prism')]