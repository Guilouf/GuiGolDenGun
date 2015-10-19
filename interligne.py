import os, os.path
import nltk
from email.parser import Parser

filepath = "C:/Users/Guigui/Desktop/M2/ADT/Moteur_Recherche/archives_SFBI/2015_06_10-bioinfo_archives_annee_2014/bioinfo_2014-01/"
listdefich = os.listdir(filepath)

def parset(listdefich,filepath):
    
    for j in listdefich:
        if ".recoded" in j:
            fichmail = open(filepath+j,"r")
            fichmail = fichmail.readlines()
            if fichmail[1] == "\n":
                for i in fichmail:
                    
            
parset(listdefich,filepath)