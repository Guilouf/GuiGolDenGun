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
                
                IMPOSER UNE LIMITE DE TAILLE AUX MOT!!
                
"""
eq= "Équipe" #\x89 
eq = eq.lower()#putain génial python 3.4 l'a resolu!!!!!!!!!!!!!!!!!
print (eq)
afiltrer = ["d'habitude","d'habitude.","fonction.","l'u=ne.", "https://sso-cas.univ-rennes1.fr/", "##########" , eq,"aujourd'hui", "goût" ,u"être",'@', "================", "*date","tahi@ibisc.univ-evry.fr",  "date*", "sun, 5 jan 2014 17:56:07 +0100",   "stage\xc2\xa0", "rôle", "français(deuxième mail)" ,   "ibañiez(tildé)"]
#filtre = ["(.)?'", ".?"]
filtre = ["(.)?'", ".?"]


regcomp = re.compile( r"(.?'|$\.|)((?P<mot>[ôûùéêèñïçàâ0-9A-Za-z_ @:./'-]*).?)"   ) #encore un problème avec d'habitue sans point...

for i in afiltrer:
    print ("origin:    " + i)
    #fix = re.sub(r"((.)?'|)((?P<mot>[ôûùéêèñïçàâ0-9A-Za-z_ @:-]*).?)", "\g<mot>", i ) #putain je sais pas comment j'ai fait mais genial quoi, faire un pipe pour les mails #je peux rajouter un flag re.unicode
    #fix = regcomp.sub("\g<mot>", i)
    #je pense qu'on peut retirer les : ; etc
    #faire un truc pour passer les É en é
    #supprimer ce qu'il ya dans des parenthèses
    #on met de coté les caracSpé..:((.)?'|)((?P<mot>[\xc3\xa9\xc2\xa0\xc5\x93\xa8\xae\xa7\xb4\xaa\xb1\xb9\x89\xbb0-9A-Za-z_ @:-]*).?)
    #((.)?'|\.$(?!\[.]))((?P<mot>[ôûùéêèñïçàâ0-9A-Za-z_ @.:-]*).?)\.$(?!\[.])
    
    
    
    
    
    
    
    
    
    fix = re.findall("([\w.]+)", i) #(.?')([\w]*)(\.?)?
    
    """ce qui marche:
    (\.$) trouve le dernier point
    
    """
    
    
    filtre.append(fix)
    
    
    
    print (" modif:    " + str(fix))

print (afiltrer)
print (filtre)



etre = ["être"]

print (etre)
print (len(etre[0]))