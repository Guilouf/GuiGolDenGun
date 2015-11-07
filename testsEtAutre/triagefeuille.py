# -*- coding: utf-8 -*-


#la fonction set peut rendre les occurences uniques
feuille = open("feuille.txt", "r", encoding='utf-8')
feuilletrie = open('feuilletrie.txt', 'w' , encoding='utf-8')

feuille = feuille.readlines()
#feuille = [l for l in feuille if l.strip()]

feuille = set(feuille) #prend que les éléments uniques

feuille = sorted(feuille) #le .sort() retourn none, il le fait direct..


print (str(feuille))

for ligne in feuille:
    #ligne = ligne.strip()
    feuilletrie.write(ligne)
    print (ligne)   #je ne vois aucun accent...