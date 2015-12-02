 #-*- coding: utf8 -*-
#F9 pour lancer le prog!

import operator #pour laddition des tuples
from main import Parsemail #import du premier script permettant la lecture et tokénisation des contenus du mail

"""
Convention objet python:
classes: SansEspaceAvecMaj
méthodes: minus_av_underscore
methode appelées auto: __av_double_under__
attribut: pareil_que_methodes
"""

"""
ca peut valoir le coup de supprimer la liste de nb de mot total, dans la valeur du dico, vu que ca sert à rien..
"""


class FichierIverse: #Il y a une faute au fait..  
    
    def __init__(self):
        
        ft = Parsemail()
        self.listeDmail, self.listeDmailRaci = ft.parsemail()
        print("#######################################################")
        
    """
    ############################
    FONCTION qui calcule l'effectif d'un mot dans un mail, et son effectif dans le corpus. Retourne ces données sous la forme d'un dico qui sert de fichier inversé.
    retourne aussi le nombre total de mots dans chaque mail, et aussi dans le corpus
    ############################
    """
    
    def fichInv(self,entreListMail):
        
        nbmotsDocs = [None] * len(entreListMail) #liste qui contient le nombre de mots dans chaque document ,initialisé ac le nb de docs(c mieu d'initialiser ac None)
        
        nbmotCorpus = 0 #compteur du nombre cumulé des mots dans les mails
        
        dicoInv = {} #clé: un mot, valeur:
        
        for indexmail in range(len(entreListMail)):#defile les mails
            
            countmotmail = 0 #compteur du nb de mots dans un mail, initialisé à 0
            
            for mot in (entreListMail[indexmail])[3]:#defile les mots du corps de mail. le [3] correspond au fait que ya la date est le sujet dont je ne me sert pas qui sont stockés
                
                
                countmotmail += 1
                
                if mot not in dicoInv:#premiere fois que le mot est detecté
                    
                    dicoInv[mot] = [[1,0],(indexmail,1)] #ajoute comme valeur une liste avec le nombre de fois ou le mot est présent dans le corpus(le zero ne sert à rien au final), puis des tuples, avec (numerodumail, nb_defois_oùlemot_est_dsle_mail)
                    
                else: #le mot est déja présent dans le dico
                    
                    ((dicoInv[mot])[0])[0] += 1 #ajout de 1 a liste de frequence totale
                    
                    if ((dicoInv[mot])[-1])[0] != indexmail:#la premiere occurence du mot dans ce mail ((dicoInv[mot])[-1])[0] = l'index du mail du dernier tuple du mot dans le dico...
                        (dicoInv[mot]).append((indexmail,1)) #rajoute un nouveau tuple dans la valeur du mot
                        
                    else: #prochaine occurences du mot dans le mm mail
                        (dicoInv[mot])[-1] = tuple(map(operator.add, (dicoInv[mot])[-1], (0,1) )) #mise a jour du tuple
                        
            nbmotsDocs[indexmail] = countmotmail #permet de compter le nombre de mots total dans un mail
            nbmotCorpus += countmotmail #permet de compter le nombre de mots dans le corpus
     
        return dicoInv,nbmotsDocs,nbmotCorpus
  
    
  
  
if __name__ == "__main__":    
    ft = FichierIverse()
    
    dicoInv, nbmotsdocs, nbmotCorpus = ft.fichInv(ft.listeDmailRaci)  #on peut choisir l'argument, entre raci et normal
               
    print("#########              DICO                 #############")    
    
    print(dicoInv["tarragon"])
    """
    bon ici aussi ca à l'air de marcher
    """
    
    for cle in dicoInv:
        print(cle +": ")# + str(dicoInv[cle]))
        
    print(nbmotsdocs)
    print(nbmotCorpus)
"""
Ce que tout ca retourne:
Un dictionnaire avec comme clé des mots,
et comme valeur une liste qui contient:
En premier une liste, avec en premiere valeur l'effectif total du mot( le zero après est pour la fonction de correction, pas implémentée car trop complexe)
ensuite, une sucession de tuples, qui contiennent:
en premier le numero (l'index) du document, et ensuite l'effectif du mot dans le document.
"""