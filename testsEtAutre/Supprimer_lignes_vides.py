import glob
import os
import re

## Cette fonction permet de supprimer les lignes vides des fichiers d'un repertoire et affiche les resultats sous format txt
## Cette fonction prend en parametres le chemin d'un repertoire
## Cette fonction donne en sortie des fichiers txt dans le dossier 'Traitement_Interlignes'

def Supprimer_Interligne(path):
    count=0   
    mesDossiers = glob.glob(path+"\\*")
    for dossier in mesDossiers:
        mesFichiers = glob.glob(dossier+"\\*recoded")
        for fichier in mesFichiers:
            count = count+1        
##            chaine=fichier.split(os.sep)
##            p=chaine[-2]
##            pattern0 =p[-2:]
##            pattern1 =os.path.basename(fichier)
            
            try:
                monFichier = open(fichier, "r", encoding='utf-8')
                d = os.path.dirname(path+"\\Traitement_Interlignes\\")
                if not os.path.exists(d):
                    os.makedirs(d)
##                output_file=open(path+"\\Traitement_Interlignes\\"+pattern0+'_'+pattern1,'w', encoding="utf-8")  # Le pattern0 sert à differecier les fichiers qui portent le meme nom et qui sont dans des dossiers differents
                output_file=open(path+"\\Traitement_Interlignes\\"+str(count)+".recoded",'w', encoding="utf-8")
                for line in monFichier.readlines():
                    if line.rstrip():
                        output_file.write(line)
                        
            except :
                print ("erreur")
                
            output_file.close()    
                
    
Supprimer_Interligne("C:\\Users\\Guigui\\Desktop\\M2\\ADT\\Moteur_Recherche\\archives_SFBI\\2015_06_10-bioinfo_archives_annee_2014")
#C:\Users\Guigui\Desktop\M2\ADT\Moteur_Recherche\archives_SFBI\2015_06_10-bioinfo_archives_annee_2014