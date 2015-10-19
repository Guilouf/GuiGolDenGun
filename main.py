#la premiere ligne est pour linux donc bat les couilles
# -*- coding: utf-8 -*-
"""
Encodage windows qui poserait problème: cp...
"""
import os, os.path
import nltk
import email
import pickle #serialisation
import codecs
import re

"""
class main:
    pass
    
    LISTE DE CHIERS BUGGANT:
    -1 fariza ok
    -2 nazim ok
    -3 dassaul BUUUUUUUUUG
    -4 jerome salse ok
    -5 hello bonjour BUUUUG
    -6 offre demploi ok
    -7 crb anim ok
    =>C'est un problème d'interlignes
    
    muahaha common word fr est en ansi, common word en en utf 8! magnifique C'est vraiment de la grosse merde ses fichiers
    pourquoi les chiffre d'ailleurs ds le common word fr??
    plus les subjects qui ont 3 encodages différents, et en plus en dur dans le fichier original!
"""
print "start"         
      
filepath = "C:/Users/Guigui/Desktop/M2/ADT/Moteur_Recherche/archives_SFBI/2015_06_10-bioinfo_archives_annee_2014/bioinfo_2014-01/"
pathFR = "C:/Users/Guigui/Desktop/M2/ADT/Moteur_Recherche/Outils/common_words.total_fr.txt"
pathENG = "C:/Users/Guigui/Desktop/M2/ADT/Moteur_Recherche/Outils/common_words.total_en.txt"
listdefich = os.listdir(filepath)


def stopwords(pathFR,pathENG):
    stopEN = open(pathENG, "r")
    stopFR = open(pathFR, "r")
    stoplist = []
    for i in stopEN:
        stoplist.append(i.strip().replace("_"," ")) #peut être les ', la tokenisation peut aussi poser problème. encodage correspond, c'est bon de ce coté
        #print i.strip().replace("_"," ").encode('utf-8')
    for j in stopFR:
        stoplist.append(j.strip().replace("_"," ")) #problème, c'est en ansi... mais je pense que je vais y remédier à la source... voila c'est fait.
    stoplist.extend(["al.","al","--",":"]) #ajoute les trucs chiants, peut etre à mettre au début de la liste pr opti. voir mm faire un système de fréquence pour mettre les truc a enlever les plus fréquents en avant.. mais ca sert mois grace à la reg ex.

    return stoplist

stoplist = stopwords(pathFR,pathENG)

def tokenostop(corpsmail, stoplist): #mettre les mots 
    #print corpsmail
    
    mailtokenibad = nltk.word_tokenize(corpsmail) #marche, mais encodage un peu chelou... puis marche assez mal en fait... (point esseulé, ou à la fin d'un mot. , (L')Utilisation.. /http séparé => PROBLEME DES "d'"
    """
    expression régulière:
    =          #enlève les points
                #supprimer les longues chaines de """"""" ou autre
                #supprime les d', l' etc...
    """
    mailtokeni =  []
    for i in mailtokenibad:
        fix = re.sub("((.)?'|)((?P<mot>[\xc3\xa9\xc2\xa0\xc5\x93\xa8\xae\xa2\xaf\xa7\xb4\xaa\xb10-9A-Za-z_ @:-]*).?)", "\g<mot>", i) #mots a problème: où(deuxime mail), THÉMATIQUE(et ouais putain les majuscules...), ya aussi les retours de chariot qui bugent sur ce mail.. goùt(pareil que nrmlt)
        #fix = i #pour desactiver la regex
        print fix
        if fix == '': 
            #print i #regarder les caractères supprimé par la regex.. et ca marche super!!!
            pass
        else : mailtokeni.append(fix) #regarder quand meme si ca n'a pas bouffer certains mots
    
    for i in stoplist: #parcourt la stoplist
        if i in mailtokeni:#regarde si un stop word est dans le mail
            #ici mettre un regex pour enlever les d' et les points à la fin du mot. ou adapter nltk
            mailtokeni = [x for x in mailtokeni if x != i] #comprehension list, faible complexité nrmlt: ne retourne que les éléments du mail qui sont différents du stopword
            #mettre en lowercase, faire correspondre l'encodage=>fait
        
    return mailtokeni

def parsemail(listdefich,filepath,stoplist):
    
    #j = listdefich[1] #a remplacer par un for...
    
    totalmail = []
    
    for j in listdefich:
        mailform = []
        if ".recoded" in j:   
            fichmail = codecs.open(filepath+j,"r") #bon je pense que c deja decodé peut etre
            mail = fichmail.read()
            contenumail = email.message_from_string(mail)
            
            
            mailform.append(contenumail['subject'].lower()) #faudra extraire le tag, pour lui donner un grand poids Il y a de iso8859-1 (latin1) et du utf8, même du windows 1252 selon le mail de provenance... donc à rencoder si on veut en faire qqchose.
            mailform.append(contenumail['date'].lower())
            mailform.append(contenumail['from'])
            mailtokeni = tokenostop(contenumail.get_payload().lower(),stoplist) #choppe le contenu du mail en lowercase, le problème c'est que Equipe se transforme en equipe au lieu de équipe...
            mailform.append(mailtokeni) #ici, tokeniser, lemmatiser...
    
            print("//////////////////////////////////////////////////////////////////")
            
            """
            print contenumail['subject'].lower()
            print contenumail['subject'].lower().encode()
            """
            
            
            print mailform
            totalmail.append(mailform) 
    print totalmail  



         
parsemail(listdefich,filepath,stoplist)



    
