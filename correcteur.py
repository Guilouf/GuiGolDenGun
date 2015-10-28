# -*- coding: utf8 -*-

"""
DISTANCE DE HAMMING peut être bien
pendre quel effectif? celui du document, mais pb des termes spécifiques et langue
regarder l'ordre lexico est une bonne preuve de proximité
si deux truc ont le mm effectif, choisir le plus court ou plus simple
et les accents bordel de merde!!!!!!!!!!!!!!!!!!!!!!!! faudrait faire un truc pour les enlever juste le temps de la comparaison

heu la c de l'aléatoire... c'est au niveau de listmatch que ca coince
=>trouvé! la liste des clefs est dans un ordre aléatoire, mais pk ca coince?
"""
from FichierInverse import fichInv
tuplelist = fichInv()
#tuplelist = {"bio-informatique": [5, (26, 1), (43, 1), (63, 1)] , "bioinfomatiques": [2, (26, 1), (43, 1), (63, 1)] , "bioinformatics": [3, (26, 1), (43, 1), (63, 1)], "bioinformatique":[10, (26, 1), (43, 1), (63, 1)], "biologie":[10, (26, 1), (43, 1), (63, 1)], "biologique":[6, (26, 1), (43, 1), (63, 1)] , "biologiques":[6, (26, 1), (43, 1), (63, 1)],"biologiste":[3, (26, 1), (43, 1), (63, 1)]} 

listcle = list(tuplelist.keys()) #cree une liste des clef, astuce pour ensuite eviter les doubles checks. ca limite les dégats mais c'est un peu moche qd mm je pense, qoique c pareil qu'une recherche d'index au final.. =>ordre au hasard
listematch = []
print(listcle)



"""
Selection des termes à raprocher
"""
for i in range(len(listcle)):

    for j in range(i+1,len(listcle)):#evite les double check
        moti = listcle[i]
        motj = listcle[j]

        if len(moti) >= len(motj)-1 and len(moti) <= len(motj)+1: #du coup on aun client potentiel, faut maintenant regarder le mot en detail
            #print   (moti , motj)
            #faudrait un score d'alignement, ou un morris prat..
            seq = ""
            score = 0.0
            for lettre in moti: #faudrait choisir le mot le plus long..
                seq += lettre
                if seq in motj:#faire gaffe au succession de courtes sequences, qui risque de foutre la marde...
                    score += 1
                else: 
                    #la entrerai en jeu le coup des accents égaux.
                    seq = ""
            #print ( score/max(len(moti),len(motj)) ) #le score seuil de 0.9 semble être adapté.
            if score/max(len(moti),len(motj)) >= 0.9:
                listematch.append((i,j))
    
  
"""
selectionne le meilleur terme.
penser a regarder comment ca ce passe si yen a plusieurs en concurence...
=>indentifier les mots présents dans plusieurs couples
"""
print ("\n")
print (listematch)
    
listetermAsuppr = []
for couple in listematch:
    #supprimer le terme ayant l'effectif le plus faible
    #et transferer son effectif vers l'autre!!!!!!!!!!!!            !!!!!!!!!!!!!!!!!!!!!!!!(quoique, peut être à la fois une bonne et une mauvaise idée pour la corection. en tt cas faut aussi transférer l'indexation des documents. de toute facon il y a un pb d'ordre, un mot peut être supprimé avant que son eff ne soit transféré
    #on peut ajouter des poids pour le s aussi                    #on a qu'a créer un effectif de transfert, qui sera ajouté à l'effectif principal à la fin.
    efftotmoti = ((tuplelist[ listcle[ couple[0] ] ])[0])[0]
    efftotmotj = ((tuplelist[ listcle[ couple[1] ] ])[0])[0]
    print ( efftotmoti, efftotmotj )
    
    if efftotmoti < efftotmotj:
        listetermAsuppr.append(couple[0])
        print ("SUPPR: " + str(tuplelist[ listcle[couple[0] ] ]) )
        (tuplelist[ listcle[ couple[1] ] ])[0] = [ ((tuplelist[ listcle[ couple[1] ] ])[0])[0], ((tuplelist[ listcle[ couple[0] ] ])[0])[0] + ((tuplelist[ listcle[ couple[0] ] ])[0])[1]  ] #putain la ca devient grave...
        print("SUPPR: "+listcle[couple[0] ]+" GARDE: "+listcle[couple[1] ] )
        print ("GARDE: " + str(tuplelist[ listcle[couple[1] ] ] ))
        
    elif efftotmoti > efftotmotj:
        listetermAsuppr.append(couple[1])
        print("SUPPR: " + str(tuplelist[ listcle[couple[1] ] ] ))
        (tuplelist[ listcle[ couple[0] ] ])[0] = [ ((tuplelist[ listcle[ couple[0] ] ])[0])[0], ((tuplelist[ listcle[ couple[1] ] ])[0])[0] + ((tuplelist[ listcle[ couple[1] ] ])[0])[1] ] # ca ne résout pas les problèmes d'ordre d'apparition=>ordonner les couples selon l'effectif de celui a supprimer. putain et en plus ya l'index des mails à mettre à jour..
        print("SUPPR: "+listcle[couple[1] ]+" GARDE: "+listcle[couple[0] ])
        print("GARDE: " + str(tuplelist[ listcle[couple[0] ] ] ))
        
    else:
        print ( "merde" )
        #on va choisir le plus court au début, mais normalement sur tout les texte c'est quasiment impossible d'avoir le mm effectif
        
print(listetermAsuppr)