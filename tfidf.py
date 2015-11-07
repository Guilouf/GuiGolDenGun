 #-*- coding: utf8 -*-
 
"""
 il va peut etre manquer l'info du nombre de mots dans le document...
 faudra completer, mais pas dans le fichier inversé, dans un objet à part.
 faut aussi calculer le nombre de mots du corpus.
 A priori tout ca se fait dans la fonction fichier inverse.
 !!ATTENTION!! : si l'on fait des corrections, faudra aussi modifier ces objets.
 
 sinon c'est un peu de la merde de reparcourir tout, et vraiment mal opti...
 """
from FichierInverse import FichierIverse
import math
 
"""
problème.. python execute des fonctions qui sont en dehors de la classe, donc en plus les codes sont executé deux *...


le tfidf est spécifique au mot et au document, faut donc le rajouter en 3eme position des tuples

IL YA DAUTRE FORMULES QUE LE TF IDF!
on peut faire une méthode pour calculer la norme des tf-idf( racine (somme de tf-idf au carré) ) (enfin c ce quils ont fait.. 
"""
 
 
class TfIdf:
     
    def __init__(self):
         
        fi = FichierIverse()
        self.dicoInv, self.nbmotsdocs, self.nbmotCorpus = fi.fichInv()
     
    """
     tf-idf(tj,di) = tf(tj,di) * idf(tj)
     
     en gros:
     tf(mot, document): nb de mots "mot" ds un doc "document"(2eme val du tuple), divisé par le nombre total de mots ds "document"(nb mots docs)
     idf(mot, listdedocuments): log( nbdedocuments / nbdedocu_contenantle_mot )
     
     le nb de documents contenant le mot, c'est le nombre de tuples!
    """
         
    def calcul(self):
          
        listcle = list(self.dicoInv.keys())
        tf = 0.0  
        idf = 0.0
        tf_idf = 0.0 #initialisation des floats
        sommedesTfIdfaucarre = 0.0
          
        for clemot in listcle: #parcour les mots du dico
              
            valeurclemot = self.dicoInv[clemot] #necessaire, cette copie? pe pb de pointeur etc pr la modif..
            
            idf = math.log( len(self.nbmotsdocs) / (    (len(valeurclemot)-1) ))#le -1 pour la liste
            #sur internet, yavait un +1 au diviseur...=>division par 0 etc? si un mot est présent que dans un doc, bref
            
            for indextuple in range(1,len(valeurclemot)):
                tf = (valeurclemot[indextuple])[1] / self.nbmotsdocs[ (valeurclemot[indextuple])[0] ]  #en espérant que les index de documents correspondent bien.. a vérifier
                print(tf)
                
                tf_idf = tf * idf #ya plus qu'a l'ajouter en 3eme tuple..
                sommedesTfIdfaucarre += tf_idf * tf_idf
                
                (self.dicoInv[clemot])[indextuple] +=  (tf_idf,)  #la virgule est la pr dire que tf_idf est un tuple.. unique
                print((self.dicoInv[clemot])[indextuple])
                
        norme = float(math.sqrt(sommedesTfIdfaucarre)) #pas sur que l'on doive faire le calcul des maintenant..
        return self.dicoInv, norme
    
    
        
"""
le faux main:
""" 
    
ti = TfIdf()

ti.calcul()