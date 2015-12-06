#-*- coding: utf8 -*-

from parsDemail import Parsemail 
import pickle
import os
import psutil
import math

class Recherche:
    
    def __init__(self,flagRACI=True, POIDS=1): #valeur par defaut, permet une sorte de surcharge
        
        self.flagRACI = flagRACI
        self.poids = POIDS
        """
        self.listmotreq = []
        ici!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """
        with open("dicotfidf", 'rb') as dicoPKL: #ouvre le fichier inverse serialisé
            self.dicoInv= pickle.load(dicoPKL)
        
        
    def traitement_requete(self,requete):
        
        dicoreq =  {}
        requete = requete.lower()
        
        parse = Parsemail(False) #dans l'initialisation de parsmail la detection et le trie des noms de fichier des mails est inutile..
        stoplist = parse.stopwords() 
        
        if self.flagRACI == True :
            listmotreqRACI = (parse.tokenostop(requete, stoplist))[1]
            listmotreq = (parse.tokenostop(requete, stoplist))[0]
        else:
            listmotreq = (parse.tokenostop(requete, stoplist))[0] #[0] pr le non racinisé
            
        
        #on ne calcule que le tf, car idf = log( nbdedocuments / nbdedocu_contenantle_mot ) = log(1/1) = 0

        """
        vérifier que le mot soit ds le grand dico...=>c'est vérifié, mais le tf est calculé avec la présence
        du mot. Ceci dit, ca reste cohérent du coup.
        """
        
        for mot in listmotreq:
            if mot not in dicoreq:
                dicoreq[mot] = float( 1 / len(listmotreq) ) #calcule le tf
            else:
                dicoreq[mot] += float( 1 / len(listmotreq) ) #update le tf si plusieurs * le mm mot ds la requète
        
        if self.flagRACI == True :        
            for mot in listmotreqRACI:
                if mot not in dicoreq:
                    dicoreq[mot] = (float( 1 / len(listmotreq) ) / self.poids )#calcule le tf
                else:
                    dicoreq[mot] += (float( 1 / len(listmotreq) ) / self.poids ) #update le tf si plusieurs * le mm mot ds la requète
        
        return dicoreq
        
    def rech(self,dicoreq):
        """
        l'idée est de récuperer la liste de tous les docs contenant un des mots de la requete,
        et ensuite pr chaque document, calculer la somme des produit du tf du mot de la req, et du tfidf de ce mot pour le doc..
        ensuite on divise le truc obtenu par la norme.
        """
        listmotreq = list(dicoreq.keys())   #c'est idiot!!! ca a déja été créé, faut le passer en self
        
        dicoinvSimpl = {}
        listdedocs = []
        
        for motreq in listmotreq:
            
            if motreq in self.dicoInv: #au cas ou un mot n'est pas dans le corpus, controle si le mot est bien dans le dico.
                
                print(motreq)
                dicoinvSimpl[motreq] = self.dicoInv[motreq]
                
                for indextuple in range(1, len(dicoinvSimpl[motreq]) ): #sert a creer la liste de docs
                    tutuple = (dicoinvSimpl[motreq])[indextuple]
                    #print(tutuple)
                    
                    if tutuple[0] not in listdedocs:
                        listdedocs.append(tutuple[0])
        
        listdedocs = sorted(listdedocs) #faire gaffe à ca, nrmlt c'est bon
        """
        et ca c koi????????????(lismtoreq)
        """
        listmotreq = list(dicoinvSimpl.keys())
        
        listcos = [] #liste les cosinus(enfin..) des documents. ds le mm ordre que listdedocs
        listPoidQcar = []
        listPoidDcar = []
        
        for doc in listdedocs:#parcourt les docs
                  
            cos = 0.0 #truc 
            sommePoidQ = 0.0
            sommePoidD = 0.0
            
            for motreq in listmotreq:#parcours les mots de la requete
                dicoinvSimpl[motreq] 
                
                
                for indextuple in range(1, len(dicoinvSimpl[motreq]) ): #parcours les tuples correspondant aux documents            le pb c que ca parcour parfois pour rien qd le doc ne contient pas le mot...
                    
                    if ((dicoinvSimpl[motreq])[indextuple])[0] == doc:#si le doc ds le tuple correspont au doc de la liste des docs retenus
                        
                        sommePoidQ += dicoreq[motreq] * dicoreq[motreq]
                        sommePoidD += ((dicoinvSimpl[motreq])[indextuple])[2] * ((dicoinvSimpl[motreq])[indextuple])[2]
                        cos += ((dicoinvSimpl[motreq])[indextuple])[2] * dicoreq[motreq] #tfidf du mot ds le doc * tf du mot ds la req
            listPoidDcar.append(sommePoidD)
            listPoidQcar.append(sommePoidQ)
            listcos.append(cos)
        
        listcosnorm = []
        
     
        for indexcosi in range(len(listcos)):#faire un compteur
            norme = math.sqrt( listPoidDcar[indexcosi] + listPoidQcar[indexcosi] )
            cosnorm = float( listcos[indexcosi] / norme )
            
            listcosnorm.append(cosnorm)
        

        #print(listdedocs)
        #print(listcosnorm)
        #print(sorted(listcosnorm, reverse=True))
        #faut trier les deux listes dans l'ordre de listcosnorm
        
        if len(listdedocs) != 0:
            listcosnorm,listdedocs = zip(*sorted(zip(listcosnorm,listdedocs), reverse = True))#tri des documents en fonction de leur cos
            #print(listdedocs)
            final_index=[]            
            for ele in listdedocs:
                final_index.append(ele+1) #pr faire correspondre l'index avec les noms des fichiers
            print("Index mail par ordre décroissant de pertinence : "+str(final_index))
            return final_index
        # Traitement de "l'exception" en cas d'absence du resultat
        else:
            print ("Aucun résultat corespondant à votre requête")
            
        
            
if __name__ == "__main__":         
    rec = Recherche(True) #true = raci
    print(rec.dicoInv["tarragon"])
    dicoreq = rec.traitement_requete("tarragona") #tarragona spain genomes biology biologie
    
    rech = rec.rech(dicoreq)
    print(dicoreq)
    
    process = psutil.Process(os.getpid())
    print(process.memory_info().rss / 1000000) #rss : resident set size
    print(process.cpu_times())