# -*- coding: utf-8 -*-
import os, os.path
import nltk
import email

#bon en gros faudra passer par email parser...

filepath = "C:/Users/Guigui/Desktop/M2/ADT/Moteur_Recherche/archives_SFBI/2015_06_10-bioinfo_archives_annee_2014/bioinfo_2014-01/"
listdefich = os.listdir(filepath)
    
def  degross(filepath,listdefich):
    
    totalmail = []
    
    for j in listdefich: #parcourt les fichiers
        
        
        finmerdier = False 
        contenumail = []
        
        if ".recoded" in j: #pour ne pas chopper le non recod
            fichmail = open(filepath+j,"r") #les recoded font bugger en fait(encoage a mettre)  marche tjr pas
            #print (fichmail[5])
            
            for i in fichmail: # il recherche dans la totalit� de la phrase ou il ny est pas=>regarder le premier element de la liste de la phrase
                
                if finmerdier== True and i !="\n":# pour avoir le texte, et eviter les lignes vides
                    #print(i)
                    contenumail.append(i)#ca marche, mais par contre c'est par ligne alors qu'il faudrait mieux en vrac (fichmail[i::]?)
                    #print contenumail
                    #faudrait chopper tt le texte d'un coup et mettre en break ici
                    pass
                if "From:" in i: #pas bon
                    contenumail.append(i)
                    pass
                if "Date:" in i:        #putain la date et le from sont pas toujours dans le mm ordre, enfin ca a l'air d'etre un bleme plus profond
                    contenumail.append(i)
                    pass    
                if "Subject:" in i: 
                    contenumail.append(i)
                    finmerdier = True
                    
            totalmail.append(contenumail)
            print (contenumail)
    return totalmail
        
totalmail = degross(filepath,listdefich)


def ecriveur(totalmail):
    dataset = open("BIGdata.csv","w")   #bon ya des sujets qui sont placés en bout de liste, comme ca... et ca change entre openoff et notepad..
    
    for i in totalmail: #parcourt les mails
        
        for j in i: #parcourt les mots du mail
            dataset.write(j.strip()) #enleve les \n
            dataset.write(';')
        dataset.write("\n")
        
ecriveur(totalmail)