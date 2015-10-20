# -*- coding: utf-8 -*-


#la fonction set peut rendre les occurences uniques
feuille = open("feuille.txt", "r")
feuilletrie = open('feuilletrie.txt', 'w')

feuille = feuille.readlines()
#feuille = [l for l in feuille if l.strip()]

feuille = set(feuille) #prend que les éléments uniques

feuille = sorted(feuille) #le .sort() retourn none, il le fait direct..


print str(feuille)

for ligne in feuille:
    #ligne = ligne.strip()
    feuilletrie.write(ligne)
    print ligne