 #-*- coding: utf8 -*-
from FichierInverse import FichierIverse
import math
import pickle #permet d'effectuer une serialisation
import psutil #permet de visualiser le temps d'exécution
import os
"""

le tfidf est spécifique au mot et au document, faut donc le rajouter en 3eme position des tuples

IL YA DAUTRE FORMULES QUE LE TF IDF!
on peut faire une méthode pour calculer la norme des tf-idf( racine (somme de tf-idf au carré) ) 
"""
 
 
class TfIdf:
     
    def __init__(self,flagRaci):
         
        fi = FichierIverse()
        if flagRaci == True:
            self.dicoInv, self.nbmotsdocs, self.nbmotCorpus = fi.fichInv(fi.listeDmailRaci)
            self.suffixe = ""  #on oublie ca en fait "RACI"
        else: 
            self.dicoInv, self.nbmotsdocs, self.nbmotCorpus = fi.fichInv(fi.listeDmail)
            self.suffixe = ""
        """    
        with open("dicotfidf", 'rb') as dicoPKL: #ouvre le fichier inverse serialisé
            self.dicoInv= pickle.load(dicoPKL)
            
        with open("norme", 'rb') as normePKL: #ouvre la norme serialisée
            self.norme= pickle.load(normePKL)
        """
    """
     tf-idf(tj,di) = tf(tj,di) * idf(tj)
     
     en gros:
     tf(mot, document): nb de mots "mot" ds un doc "document"(2eme val du tuple), divisé par le nombre total de mots ds "document"(nb mots docs)
     idf(mot, listdedocuments): log( nbdedocuments / nbdedocu_contenantle_mot )
     
     le nb de documents contenant le mot, c'est le nombre de tuples!
    """
         
    def calcul(self):
        """
        faut spécifier les noms de dico de sortie
        """  
        
        listcle = list(self.dicoInv.keys())
        """
        Initialisation des floats
        """
        tf = 0.0  
        idf = 0.0
        tf_idf = 0.0 
        sommedesTfIdfaucarre = 0.0
          
        for clemot in listcle: #parcourt les mots du dico
              
            valeurclemot = self.dicoInv[clemot] #necessaire, cette copie? pe pb de pointeur etc pr la modif..
            
            idf = math.log( len(self.nbmotsdocs) / (    (len(valeurclemot)-1) ))#le -1 pour la liste a supp ds la valeur
            """
            #sur internet, yavait un +1 au diviseur...=>division par 0 etc? si un mot est présent que dans un doc, bref
            OPTIMISER!!!!!!!!!!!!!!!!!!!!!!?? pas forcément évident..
            """
            for indextuple in range(1,len(valeurclemot)): #parcourt les tuples de la valeur du mot, qui contiennent l'index du doc et le nb de fois ou le mot y est présent
                
                tf = (valeurclemot[indextuple])[1] / self.nbmotsdocs[ (valeurclemot[indextuple])[0] ]  #calcule le tf du mot
                
                tf_idf = tf * idf #calcule le tf-idf du mot pour le document
                sommedesTfIdfaucarre += tf_idf * tf_idf #a utiliser pour la norme
                
                (self.dicoInv[clemot])[indextuple] +=  (tf_idf,)  #ajoute le tf-idf à la fin du tuple(la virgule est la pr dire que tf_idf est un tuple.. unique)
                #print((self.dicoInv[clemot])[indextuple])
                
        self.norme = float(math.sqrt(sommedesTfIdfaucarre)) #calcule la norme des tf-idf
        
        
            
        return self.dicoInv, self.norme  #ya pas une couille avc le fait d'utiliser le mm objet initialisé au départ??? puis putain il sert a rien le return!
    
    def serialisation(self,flagAPPEND):
        
        if flagAPPEND == False:#on écrase les anciens dico
            with open("dicotfidf"+self.suffixe, 'wb') as dicotfidfPKL: #serialise le fichier inverse contenant les tf-idf...
                pickle.dump(self.dicoInv,dicotfidfPKL)
                
            with open("norme"+self.suffixe, 'wb') as normePKL: #serialise la norme
                pickle.dump(self.norme,normePKL)
                
        else:#là on essaye de rajouter le nouveau dico..
            #vieuDico = {}
            #viellenorme = 0.0
            with open("dicotfidf"+self.suffixe, 'rb') as dicotfidfPKL: #serialise le fichier inverse contenant les tf-idf...
                vieuDico = pickle.load(dicotfidfPKL)
                
            #with open("norme"+self.suffixe, 'wb') as normePKL: #serialise la norme
                #pickle.dump(viellenorme,normePKL)
                
            #print(vieuDico)
            #concaténation des deux dicos..si possible ecraser la valeur raci si conflit
            self.dicoInv.update(vieuDico)
            
            with open("dicotfidf"+self.suffixe, 'wb') as dicotfidfPKL: #serialise le fichier inverse contenant les tf-idf...
                pickle.dump(self.dicoInv,dicotfidfPKL)
            
        
    
        
"""
le faux main:
""" 
if __name__ == "__main__":   
    process = psutil.Process(os.getpid()) 
    ti = TfIdf(True) #si true, racinisation. false, normal 
    ti.calcul()
    ti.serialisation(False)
    
    ti2 = TfIdf(False)
    ti2.calcul()
    ti2.serialisation(True)
    print(ti.dicoInv["tarragon"])
    print(ti2.dicoInv["tarragona"])#donc dicoInv est devenu nonetype...
    
    with open("dicotfidf", 'rb') as dicoPKLtest: #ouvre le fichier inverse serialisé
            dicoInvtest= pickle.load(dicoPKLtest)
    print(dicoInvtest["tarragon"])
    print(dicoInvtest["tarragona"])
    """
    ok alors tout ce que ca sort est en racinisé...
    """
    
    print( "Mémoire utilisée(en Mo): " , process.memory_info().rss / 1048576)
    print(process.cpu_times())