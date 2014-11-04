dotatreasures
=============

Small program to determine which Treasure to redeem given personal preferences
regarding hero use and cosmetic set quality.  Preference data is generated using
the `create_heroes_json.py` and `create_treasures_json.py` scripts and stored in
the two JSON files.  The answer is then computed by running `crunch.py`

Results on 3 Nov '14: 

    [(6.75, u'Treasure of the Eternal Alliance'),
     (5.75, u"Treasure of the Summit's Peak"),
     (5.6, u'Treasure of the Tangled Keepsake'),
     (5.5, u"Treasure of the Mender's Palm"),
     (5.0, u'Treasure of the Forged Fury'),
     (4.875, u'Treasure of the Rotted Gallows'),
     (4.5, u'Treasure of the Onyx Eye'),
     (4.0, u"Treasure of the Cannon's Fuse"),
     (2.6, u'Treasure of the Elemental Trophy'),
     (2.0, u'Treasure of the Fractured Prism')]
