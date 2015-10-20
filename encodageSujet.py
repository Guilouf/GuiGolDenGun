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
from email.header import decode_header, make_header


filepath = "C:/Users/Guigui/Desktop/M2/ADT/Moteur_Recherche/archives_SFBI/2015_06_10-bioinfo_archives_annee_2014/bioinfo_2014-01/"
listdefich = os.listdir(filepath)




def parsemail(listdefich,filepath):
    
  
    
    totalmail = []
    
    for j in listdefich:
        mailform = []
        if ".recoded" in j:   
            fichmail = codecs.open(filepath+j,"r") #bon je pense que c deja decodé peut etre
            mail = fichmail.read()
            contenumail = email.message_from_string(mail)
   
            sujet = contenumail['subject']
            print sujet
            convsuje = decode_header(sujet)
            print str(convsuje)
            default_charset = 'UTF-8'
            print ' '.join([ unicode(t[0], t[1] or default_charset) for t in convsuje ])
            print("//////////////////////////////////////////////////////////////////")
            
            """
            print contenumail['subject'].lower()
            print contenumail['subject'].lower().encode()
            """
            
            
            print mailform
            totalmail.append(mailform) 
    print totalmail  



parsemail(listdefich,filepath)