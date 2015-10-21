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
eq = eq.lower()#putain génial python 3.4 l'a resolu!!!!!!!!!!!!!!!!!
print (eq)
afiltrer = ["d'habitude","fonction.","l'une.", "##########" , eq,"où", "goût" ,u"être",'@', "================", "*date","tahi@ibisc.univ-evry.fr", "sun, 5 jan 2014 17:56:07 +0100", "master/ing\xc3\xa9nieur", "esp\xc3\xa8ces", "stage\xc2\xa0","ma\xc3\xaetres","même", "contôlé", "rôle", "français(deuxième mail)" , "thêmatique", "comité", "ibañiez(tildé)"]
filtre = ["(.)?'", ".?"]


for i in afiltrer:
    print ("origin:    " + i)
    fix = re.sub(r"((.)?'|)((?P<mot>[ôûùéêèñïçàâ0-9A-Za-z_ @:-]*).?)", "\g<mot>", i ) #putain je sais pas comment j'ai fait mais genial quoi, faire un pipe pour les mails #je peux rajouter un flag re.unicode
    #je pense qu'on peut retirer les : ; etc
    #faire un truc pour passer les É en é
    #supprimer ce qu'il ya dans des parenthèses
    #on met de coté les caracSpé..:((.)?'|)((?P<mot>[\xc3\xa9\xc2\xa0\xc5\x93\xa8\xae\xa7\xb4\xaa\xb1\xb9\x89\xbb0-9A-Za-z_ @:-]*).?)
    
    
    
    print (" modif:    " + fix)

print (afiltrer)


uetre = [u"être"]

print (uetre)
print (len(uetre[0]))

etre = ["être"]

print (etre)
print (len(etre[0]))