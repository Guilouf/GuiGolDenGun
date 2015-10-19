## Cette fonction permet de supprimer les lignes vides des fichiers d'un repertoire et affiche les resultats sous format txt
## Cette fonction prend en parametres le chemin d'un repertoire
## Cette fonction donne en sortie des fichiers txt 

def Supprimer_Interligne(path):
    import glob
    import os
    import re
    mesDossiers = glob.glob(path+"\\*")
    for dossier in mesDossiers:
        mesFichiers = glob.glob(dossier+"\\*")
        for fichier in mesFichiers:
            chaine=fichier.split(os.sep)
            p=chaine[-2]
            pattern0 =p[-2:]
            pattern1 =os.path.basename(fichier)
            monFichier = file(fichier)
            output_file=open(path+"\\"+pattern0+'_'+pattern1+"_Traite.txt",'w')
            for line in monFichier.readlines():
                if line.rstrip():
                    output_file.write(line)
    output_file.close()    
    
Supprimer_Interligne("C:\\Users\\Sofiane\\Desktop\\M2_BIG\\ADT\\Projet_2015\\Donnees\\archives_SFBI\\archives_SFBI\\2015_06_10-bioinfo_archives_annee_2014")

