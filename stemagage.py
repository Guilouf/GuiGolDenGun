# -*- coding: utf8 -*-

import nltk.stem.snowball 

feuilletrie = open('feuilletrie.txt' , 'r')

feuilletrie = feuilletrie.readlines()

stemAl = nltk.stem.snowball.FrenchStemmer()

"""
pas trop mal, mais penser à éliminer toutes les érreurs d'encodage car un caractère mal encodé et tt s'arrète. les accents sont bien pris en compte.
mais qq bugs: cnrs transformé en cnr..
"""


for mot in feuilletrie:
    mot = mot.strip().decode('utf-8')
    stema = stemAl.stem(mot)
    print stema