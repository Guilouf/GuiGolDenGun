 #-*- coding: utf8 -*-
#F9 pour lancer le prog!

#penser ensuite à la serialisation, à voir
import main
import operator #pour laddition des tuples
from main import Parsemail

"""
Convention objet python:
classes: SansEspaceAvecMaj
méthodes: minus_av_underscore
methode appelées auto: __av_double_under__
attribut: pareil_que_methodes
"""

"""
ca peut valoir le coup de supprimer la liste de nb de mot total, dans la valeur du dico..
"""


class FichierIverse: #ya une faute au fait..
       
    
    
    def __init__(self):
        
        ft = Parsemail()
        self.listeDmail = ft.parsemail()
        print("#######################################################")
        
    """
    calculer le nb de mots total dans chaque documents, et dans le corpus.
    """
    def fichInv(self):
        
        nbmotsDocs = [None] * len(self.listeDmail) #initialiser ac le nb de docs(c mieu d'initialiser ac None
        nbmotCorpus = 0
        
        dicoInv = {} #pas sur qu'un dico soit une si bonne idée..
        
        for indexmail in range(len(self.listeDmail)):#defile les mails
            #print(mess[3])
            countmotmail = 0
            
            for mot in (self.listeDmail[indexmail])[3]:#defile les mots du coprs de mail
                
                countmotmail += 1
                
                if mot not in dicoInv:#premiere fois que le mot est detecté
                    #freqmess = 1
                    #print("merde") #faut faire un dictionnaire de tuples.. ptetre pas une bonne idée les tuples en fait
                    dicoInv[mot] = [[1,0],(indexmail,1)] #frequence totale=> au lieu d'indexmail, faire tuple indexmail + freq dans le mail..
                    
                else: #le mot est déja présent dans le dico
                    #freqmess = (dicoInv[mot])[1]+1 #ouais mais non...: il faut que cette frequence soit associée à chaque message..
                    #dicoInv[mot] = tuple(map(operator.add, dicoInv[mot], (1,freqmess) ))
                    ((dicoInv[mot])[0])[0] += 1 #ajout de 1 a liste de frequence totale
                    
                    if ((dicoInv[mot])[-1])[0] != indexmail:#la premiere occurence du mot dans ce mail ((dicoInv[mot])[-1])[0] = l'index du mail du dernier tuple du mot dans le dico...
                        (dicoInv[mot]).append((indexmail,1))
                    else: #prochaine occurences du mot dans le mm mail
                        (dicoInv[mot])[-1] = tuple(map(operator.add, (dicoInv[mot])[-1], (0,1) ))
                        
            nbmotsDocs[indexmail] = countmotmail 
            nbmotCorpus += countmotmail           
     
        return dicoInv,nbmotsDocs,nbmotCorpus
  
  
  
  
if __name__ == "__main__":    
    ft = FichierIverse()
    dicoInv, nbmotsdocs, nbmotCorpus = ft.fichInv()
               
    print("#########              DICO                 #############")    
    ""    
    print(str(dicoInv))
    
    for i in dicoInv:
        print(i +": "+ str(dicoInv[i]))
        
    print(nbmotsdocs)
    print(nbmotCorpus)
"""
Ce que tout ca retourne:
Un dictionnaire avec comme clé des mots,
et comme valeur une liste qui contient:
En premier une liste, avec en premiere valeur l'effectif total du mot( le zero après est pour la fonction de correction)
ensuite, une sucession de tuples, qui contiennent:
en premier le numero (l'index) du document, et ensuite l'effectif du mot dans le document.
"""