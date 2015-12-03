#-*- coding: utf8 -*-
from parsDemail import Parsemail
from FichierInverse import FichierIverse
from tfidf import TfIdf
from recherche import Recherche
import os
import psutil

"""
#################
Chemins d'accès des fichiers: ce serait pas mal de les mettre en self de cette classe de sorte que les autres classes puissent l'appeler..
#################
"""
filepath = "C:/Users/Guigui/Desktop/M2/ADT/Moteur_Recherche/archives_SFBI/2015_06_10-bioinfo_archives_annee_2014/Traitement_Interlignes/"
pathFR = "C:/Users/Guigui/Desktop/M2/ADT/Moteur_Recherche/Outils/common_words.total_fr.txt"        
pathENG = "C:/Users/Guigui/Desktop/M2/ADT/Moteur_Recherche/Outils/common_words.total_en.txt"

def initialisation():
    pm = Parsemail(filepath,pathFR,pathENG)#tain c quoi déja le truc pour écraser les méthodes??la surcharge, des constructeurs
    listeDmail, listeDmailRaci = pm.parsemail()
    
    
    
    fi = FichierIverse()
    dicoInv, nbmotsdocs, nbmotCorpus =fi.fichInv(listeDmail)
    dicoInvR, nbmotsdocsR, nbmotCorpusR = fi.fichInv(listeDmailRaci)
    
    
    ti = TfIdf(False,dicoInv,nbmotsdocs,nbmotCorpus)
    ti.calcul()
    ti.serialisation()
    ti2 =TfIdf(True, dicoInvR, nbmotsdocsR, nbmotCorpusR)#le true autorise la concaténation avec l'ancien dico
    ti2.calcul()
    ti2.serialisation()

initialisation()#commenter pour faire des recherches successives

rec = Recherche(True)#le truc indique que la rechecher va se porter aussi sur les mots racinisés.
dicoreq = rec.traitement_requete("batard") #tarragona spain genomes biology biologie
    
rech = rec.rech(dicoreq)
print(dicoreq)


process = psutil.Process(os.getpid())
print(process.memory_info().rss / 1000000) #rss : resident set size
print(process.cpu_times())

""" c'est cool ca
def __init__(self,arg1=None,arg2=None):
    if arg1 and arg2 :
        # traitement si argument 1 et 2
        ...
    else :
        # traitement si pas d'argument
       ...

"""