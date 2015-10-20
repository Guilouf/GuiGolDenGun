# -*- coding: utf-8 -*-

import re

"""
expression régulière:
    =          #enlève les points
                #supprimer les longues chaines de """"""" ou autre
                #supprime les d', l' etc...
                #les mails
                #les cractères seuls
                #certains numéros
                ((.)?'|)((?P<mot>\w*).?)
"""
eq= "Équipe" #\x89 
eq = eq.lower()
print eq
afiltrer = ["d'habitude","fonction.","l'une.", "##########" , eq,"où", "goût" ,'@', "================", "*date","tahi@ibisc.univ-evry.fr", "sun, 5 jan 2014 17:56:07 +0100", "master/ing\xc3\xa9nieur", "esp\xc3\xa8ces", "stage\xc2\xa0","ma\xc3\xaetres","même", "contôlé", "rôle", "français(deuxième mail)" ,"être", "thêmatique", "comité", "ibañiez(tildé)"]
filtre = ["(.)?'", ".?"]


for i in afiltrer:
    print "origin:    " + i
    fix = re.sub(ur"((.)?'|)((?P<mot>[\xc3\xa9\xc2\xa0\xc5\x93\xa8\xae\xa7\xb4\xaa\xb1\xb9\x89\xbb0-9A-Za-z_ @:-]*).?)", "\g<mot>", i) #putain je sais pas comment j'ai fait mais genial quoi, faire un pipe pour les mails
    #je pense qu'on peut retirer les : ; etc
    #faire un truc pour passer les É en é
    
    
    
    print "modif:    " + fix
    
print afiltrer