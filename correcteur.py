# -*- coding: utf8 -*-

"""
DISTANCE DE HAMMING peut être bien
pendre quel effectif? celui du document, mais pb des termes spécifiques et langue
regarder l'ordre lexico est une bonne preuve de proximité
si deux truc ont le mm effectif, choisir le plus court ou plus simple
"""

tuplelist = [("bio-informatique", 5),("bioinfomatiques", 2), ("bioinformatics", 3), ("bioinformatique",10), ("biologie",10),("biologique", 6), ("biologiques",6),("biologiste",3) ]

listematch = []
"""
Selection des termes à raprocher
"""
for i in range(len(tuplelist)):

    for j in range(i+1,len(tuplelist)):#evite les double check
        moti = (tuplelist[i])[0]
        motj = (tuplelist[j])[0]

        if len(moti) >= len(motj)-1 and len(moti) <= len(motj)+1: #du coup on aun client potentiel, faut maintenant regarder le mot en detail
            print   moti , motj
            #faudrait un score d'alignement, ou un morris prat..
            seq = ""
            score = 0.0
            for lettre in moti: #faudrait choisir le mot le plus long..
                seq += lettre
                if seq in motj:
                    score += 1
                else: 
                    #la entrerai en jeu le coup des accents égaux.
                    seq = ""
            print score/max(len(moti),len(motj)) #le score seuil de 0.9 semble être adapté.
            if score/max(len(moti),len(motj)) >= 0.9:
                listematch.append((i,j))
    
    
"""
selectionne le meilleur terme.
penser a regarder comment ca ce passe si yen a plusieurs en concurence...
"""
print "\n" 
print listematch
    
listetermAsuppr = []
for couple in listematch:
    #supprimer le terme ayant l'effectif le plus faible
    effmoti = (tuplelist[couple[0]])[1]
    effmotj = (tuplelist[couple[1]])[1]
    print effmoti, effmotj
    
    if effmoti < effmotj:
        listetermAsuppr.append(couple[0])
        print tuplelist[couple[0]]
        
    elif effmoti > effmotj:
        listetermAsuppr.append(couple[1])
        tuplelist[couple[1]]
    else:
        print "merde"
        #on va choisir le plus court au début