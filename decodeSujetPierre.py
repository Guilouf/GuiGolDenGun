 #-*- coding: utf8 -*-
from email.header import decode_header
import email
import pickle #serialisation
import codecs
import re
from email.header import decode_header, make_header
import os, os.path



filepath = "C:/Users/Guigui/Desktop/M2/ADT/Moteur_Recherche/archives_SFBI/2015_06_10-bioinfo_archives_annee_2014/bioinfo_2014-01/"
listdefich = os.listdir(filepath)

msg = codecs.open(filepath+"1","r" , encoding='utf-8')


ugly_subject = msg.get('subject', None)

# No subject in header
if ugly_subject is not None:

    # Multiple spaces (2)
    ugly_subject = re.sub('[ ]{2}', '', ugly_subject)
    r = decode_header(ugly_subject)

    # No decoding required => [(entire chain)]
    if len(r) > 1:
        # Subject does not meet the RFC2047 :-(
        try:
            clean_subject = ''.join(txt.decode(enc or "utf-8") 
                                    for txt, enc in r)
        except:
            clean_subject = "ERROR: " + email_file_path + \
                            ";" + ugly_subject
        finally:
            s_file.write(clean_subject + '\n')