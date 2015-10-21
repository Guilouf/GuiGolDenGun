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
from numexpr.necompiler import getType



filepath = "C:/Users/Guigui/Desktop/M2/ADT/Moteur_Recherche/archives_SFBI/2015_06_10-bioinfo_archives_annee_2014/bioinfo_2014-01/"
listdefich = os.listdir(filepath)




def parsemail(listdefich,filepath):
    
  
    
    totalmail = []
    
    for j in listdefich:
        mailform = []
        if ".recoded" in j:   
            fichmail = open(filepath+j,"r" , encoding='utf-8') #bon je pense que c deja decodé peut etre
            mail = fichmail.read()
            contenumail = email.message_from_string(mail)
   
            sujet = contenumail['subject'].lower()
            #print (sujet)
            convsuje = decode_header(sujet)
            print ("convsuj:       " + str(convsuje))
            #print ( ' '.join(txt.decode(enc or "utf-8") for txt, enc in convsuje))
            print("//////////////////////////////////////////////////////////////////")
            
            #on va faire un truc simple pas de comprehension de liste...
            for i in convsuje:#parcourt les tuple de mot du sujet
                #print ("start:      " + str(i[0]))
                #print (str(type(i[0])) + str(type(i[1])) )
                
                if type(i[0]) is str and i[1] is None : #resumons: les bytes not encode, et str not decode...
                    i[0].encode('utf-8')
                    print (i[0])
                    print("none!!!str")
                if type(i[0]) is  bytes and i[1] is None :
                    print(i[0].decode('utf-8'))
                    print("none!!!bytes")
                if type(i[0]) is  bytes and i[1] is not None:
                    print(i[0].decode(i[1]))
                    print("ENCODAGE: "+str(i[1])+" !!!bytes")
            ""
            """
             print ( ' '.join([ unicode(t[0], t[1] or default_charset) for t in convsuje ]) )
            print contenumail['subject'].lower()
            print contenumail['subject'].lower().encode()
            """
            
            
            #print ( mailform )
            totalmail.append(mailform) 
    #print ( totalmail)



parsemail(listdefich,filepath)