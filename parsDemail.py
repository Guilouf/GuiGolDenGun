#la premiere ligne est pour linux donc bat les couilles
# -*- coding: utf-8 -*-

import os, os.path #chemins de fichier
import nltk #outils pour tokenisation
from nltk.stem.snowball import SnowballStemmer #racinisation
import email #pour parser les mails
import re #expression regulières


"""
Les fichiers common word FR et EN doivent être en utf-8, et les nombre inutiles du FR supprimés.
    
penser à proposer de download les fichier nltk pour lancer le truc sur une autre machine
    
    
faire un fichier inversé ac les mots originaux et l'index de liste de leur racine.
faire une correction dans le fichier inversé pour regrouper en un seul mot ceux ayants des fautes, ac la forme retenue etant celle ayant le + grd effectif
"""
"""
INTEGRER des arguments pour créer les paths..
"""


class Parsemail:

    def __init__(self,filepath,pathFR,pathENG):
        
        print("start __init__ parsemail" )        
        
            
        self.filepath = filepath 
        
        self.pathFR = pathFR
        
        self.pathENG = pathENG
        
        listdefichenbordel = os.listdir(self.filepath)
        self.listdefich = sorted(listdefichenbordel, key = lambda num: int(num[:-8]) ) #""" permet de trier les fichiers selon l'ordre numérique (attention, faut que les fichiers aient bien .recoded à la fin...)"""
        
        
        self.stoplist = self.stopwords() 
        
        self.raciniseur = SnowballStemmer("french")
    
    """
    ############################
    FONCTION qui crée une liste à partir des fichiers de stop words anglais et et francais, et plus quelques ajouts personnels
    APPELEE dans: le main
    PB: c'est-à-dire: stopword, mais la reg ex enlève le c'..=====>appliquer une regex aux stop words
    ############################
    """
    def stopwords(self):
        stopEN = open(self.pathENG, "r", encoding='utf-8')
        stopFR = open(self.pathFR , "r", encoding='utf-8')
        stoplist = []
        for i in stopEN:
            stoplist.append(i.strip().replace("_"," ")) #remplace les _ par des " " pour matcher avec les mots du texte
            #print i.strip().replace("_"," ").encode('utf-8')
        for j in stopFR:
            stoplist.append(j.strip().replace("_"," ")) 
        stoplist.extend(["al.","al","-","--",":","@"]) #ajoute des stops words spécifiques au corpus
    
        return stoplist
    
                               
    """
    ############################
    FONCTION qui tokenise le corps du mail, et y enlève les stopwords
    APPELEE dans: parsemail
    ############################
    """
    def tokenostop(self,corpsmail, stoplist): 
        
        mailtokenibad = nltk.word_tokenize(corpsmail) #fonction de nltk qui tokenise les mots du corps du mail
        #(point esseulé, ou à la fin d'un mot. , PROBLEME DES "d'" => expressions régulières
        """
        et si tu mettait l'option french connard????????????????????????????????????????
        """
       
        mailtokeni =  [] #liste qui contient les mots tokenisés et corrigés d'un document
        mailracini = [] #liste qui contient les mots racinisés
        
        for i in mailtokenibad: #parcourt les mots tokénisés par nltk
            fix = re.sub("((.)?'|)((?P<mot>[ôûùéêèñïçàâA-Za-z_ @:-]*).?)", "\g<mot>", i) #expression régulière pour corriger les ratés de la fonction nltk
            """
            faut refaire le truc d'avant
            """
            #mots a problème:  aujourd'hui
            #fix = i #décommenter pour desactiver la regex
            #print fix
            if fix == '' or fix in stoplist: # si un "mot" à été supprimé par la regex, permet de ne pas l'ajouter dans la liste finale. ou alors le mot est un stopword
                pass
            else : 
                #print(fix)
                mailtokeni.append(fix) #ajoute le mot bien tokenisé dans la liste. peut contenir des stopwords
                mailracini.append(self.raciniseur.stem(fix)) #faire un flag pour désactiver si besoins
                #bon apparement l'ancienne méthode coutait moins de temps...
                
        """
        A OPTIMISER!
        =>fait mais ca change rien.. par contre ca pompe beaucoup les stopwords
        
        for i in stoplist: #parcourt la stoplist
            if i in mailtokeni:#regarde si un stop word est dans le mail
                #print(i) #print le stopword en commun
                #ici mettre un regex pour enlever les d' et les points à la fin du mot. ou adapter nltk
                mailtokeni = [x for x in mailtokeni if x != i] #comprehension list, faible complexité nrmlt: ne retourne que les éléments du mail qui sont différents du stopword
        """        
            
        return mailtokeni, mailracini
    
    
    """
    ############################
    FONCTION pour extraire le contenu des mails, et le separé en une liste de 3 éléments
    APPELEE dans: le main
    ############################
    """
    
    def parsemail(self): #listdefich,filepath,stoplist
        
        totalmail = [] #liste qui contient mailform
        totalmailraci = []
        
        for j in self.listdefich: #parcours les fichiers contenant les mails
            
            mailform = [] #liste qui contient les différentes parties du mail: sujet, date, auteur et contenu tokénisé
            mailformraci = [None] * 4 #pour simuler le fait qu'il doit nrmlt stocker la date etc du sujet
            
            fichmail = open(self.filepath+j,"r", encoding='utf-8') #ouvre un fichier contenant un mail
            mail = fichmail.read() 
            contenumail = email.message_from_string(mail) #utilise le package email pour lire le contenu du mail
            
            
            mailform.append(contenumail['subject'].lower()) #A recoder si je veux en faire qqchose.
            mailform.append(contenumail['date'].lower())
            mailform.append(contenumail['from'])
            
            """
            je peux mettre un flag bool ici. et retourner 2 versions de total mail..
            """
            mailtokeni, mailraci  = self.tokenostop(contenumail.get_payload().lower(),self.stoplist) #contenu du mail tokenisé
            #mettre un flag pr desacti si besoins
            
     
            
            mailform.append(mailtokeni) #ajoute le contenu du mail, réinitialisé à chaque mail
            
            mailformraci[3] = mailraci #pareil simulation des infos secondaires
    
            #print("//////////////////////////////////////////////////////////////////")
            
            #print (mailform[0])
            totalmail.append(mailform) #ajoute les liste de tokens de chaque mail ds un index
            totalmailraci.append(mailformraci)
        #print (totalmail)  
        #print(self.listdefich)
        return totalmail, totalmailraci
    
    
    
    
if __name__ == "__main__": #permet de ne pas executer à l'import du fichier mais seulement qd on ne run que ce fichier
    ft = Parsemail()
          
    listeDmail, listeDmailRaci = ft.parsemail() 
    """
    for mail in listeDmail:
        for contenu in mail[3]:
            print(contenu)
     """       
    for mail in listeDmailRaci:
        for contenu in mail[3]:
            print(contenu)
    """
    print("Copie 500 fois: 'Je ne doit pas m'imprimer en dehors d'une éxécution directe '")
    for i in range(500): 
        print("Je ne doit pas m'imprimer en dehors d'une éxécution directe ")
    """


    
