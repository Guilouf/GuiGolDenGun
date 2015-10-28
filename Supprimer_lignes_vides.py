## Cette fonction permet de supprimer les lignes vides des fichiers d'un repertoire et affiche les resultats sous format txt
## Cette fonction prend en parametres le chemin d'un repertoire
## Cette fonction donne en sortie des fichiers txt 


def Supprimer_Interligne(path):
    import glob
    import os
    import re
    #print("putain")
    mesDossiers = glob.glob(path+"\\*")
    for dossier in mesDossiers:
        #print("putain?")
        mesFichiers = glob.glob(dossier+"\\*")
        for fichier in mesFichiers:
            print("putain!")
            chaine=fichier.split(os.sep)
            p=chaine[-2]
            pattern0 =p[-2:]
            pattern1 =os.path.basename(fichier)
            monFichier = open(fichier, "r", encoding='utf-8')
            output_file=open(path+"\\"+pattern1,'w', encoding="utf-8")
            for line in monFichier.readlines():
                if line.rstrip():
                    output_file.write(line)
            output_file.close()    
            
    
Supprimer_Interligne("C:\\Users\\Guigui\\Desktop\\M2\\ADT\\Moteur_Recherche\\archives_SFBI\\2015_06_10-bioinfo_archives_annee_2014")

print("putain...")