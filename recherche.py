 #-*- coding: utf8 -*-

from tfidf import TfIdf #aussi apparement..
from parsDemail import Parsemail 
import nltk #inutile
import pickle
import os
import psutil

class Recherche:
    
    def __init__(self,flagRACI=False,POIDS=1):
        
        self.flagRACI = flagRACI
        self.poids = POIDS
        
        with open("dicotfidf", 'rb') as dicoPKL: #ouvre le fichier inverse serialisé
            self.dicoInv= pickle.load(dicoPKL)
            
        with open("norme", 'rb') as normePKL: #ouvre la norme serialisée
            self.norme= pickle.load(normePKL)
    
    def traitement_requete(self,requete):
        """
        ici il faut que j'intègre les mots racinisés et non racinisé dans le dicoreq.. et si je divisait par deux le tf des racinisés? faudrait du coup avoir les raci et non racis dans le mm dico..fait, mais peut pas y avoir un pb de clés dupliquées du coup??
        """
        dicoreq =  {}
        requete = requete.lower()
        filepath = "C:/Users/Guigui/Desktop/M2/ADT/Moteur_Recherche/archives_SFBI/2015_06_10-bioinfo_archives_annee_2014/Traitement_Interlignes/"
        pathFR = "C:/Users/Guigui/Desktop/M2/ADT/Moteur_Recherche/Outils/common_words.total_fr.txt"        
        pathENG = "C:/Users/Guigui/Desktop/M2/ADT/Moteur_Recherche/Outils/common_words.total_en.txt"
        parse = Parsemail(filepath,pathFR,pathENG) #le pb c'est l'initialisation d'un instance complète de parsemail est inutile..
        stoplist = parse.stopwords() #ca serait mieux dans l'initialiseur parsDemail
        
        if self.flagRACI == True :
            listmotreqRACI = (parse.tokenostop(requete, stoplist))[1]
            listmotreq = (parse.tokenostop(requete, stoplist))[0]
        else:
            listmotreq = (parse.tokenostop(requete, stoplist))[0] #[0] pr le non racinisé
            
        
        
        #listmotreq = nltk.word_tokenize(requete, 'french')
        
        #on ne calcule que le tf, car idf = log( nbdedocuments / nbdedocu_contenantle_mot ) = log(1/1) = 0
        #a moins qu'on ne prenne en compte le corpus ds le nb de docs?
        """
        vérifier que le mot soit ds le grand dico...=>c'est vérifié un peu dans rech, mais le tf est calculé avec la présence
        du mot
        """
        for mot in listmotreq:
            if mot not in dicoreq:
                dicoreq[mot] = float( 1 / len(listmotreq) ) #calcule le tf
            else:
                dicoreq[mot] += float( 1 / len(listmotreq) ) #update le tf si plusieurs * le mm mot ds la requète
                
        for mot in listmotreqRACI:
            if mot not in dicoreq:
                dicoreq[mot] = (float( 1 / len(listmotreq) ) / self.poids )#calcule le tf
            else:
                dicoreq[mot] += (float( 1 / len(listmotreq) ) / self.poids ) #update le tf si plusieurs * le mm mot ds la requète
        
        return dicoreq
        
    def rech(self,dicoreq):
        """
        l'idée(foireuse?) est de récuperer la liste de tous les docs contenant un des mots de la requete,
        et ensuite pr chaque document, calculer la somme des produit du tf du mot de la req, et du tfidf de ce mot pour le doc..
        ensuite on divise le truc obtenu par la norme.
        
        du coup,
        """
        listmotreq = list(dicoreq.keys())
        
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
        
        listcos = [] #liste les cosinus(enfin..) des documents. ds le mm ordre que listdedocs
        for doc in listdedocs:#parcourt les docs
            
            
            cos = 0.0 #truc 
            
            for motreq in listmotreq:#parcours les mots de la requete, mais ya des mots inconnus qui passent!!!!!!!!
                dicoinvSimpl[motreq]
                
                for indextuple in range(1, len(dicoinvSimpl[motreq]) ): #le pb c que ca parcour parfois pour rien qd le doc ne contient pas le mot...
                    
                    if ((dicoinvSimpl[motreq])[indextuple])[0] == doc:
                        
                        cos += ((dicoinvSimpl[motreq])[indextuple])[2] * dicoreq[motreq] #tfidf du mot ds le doc * tf du mot ds la req
        
            listcos.append(cos)
        
        listcosnorm = []
        
        #normalisation des cos            #a faire ds la boucle plus haut
        """
        putain ya la norme aussi! et yen a 2différentes nrmlmt
        """
        for cos in listcos:
            cosnorm = float( cos / self.norme )
            listcosnorm.append(cosnorm)
        

        #print(listdedocs)
        #print(listcosnorm)
        #print(sorted(listcosnorm, reverse=True))
        #faut trier les deux listes dans l'ordre de listcosnorm
        
        if len(listdedocs) != 0:
            listcosnorm,listdedocs = zip(*sorted(zip(listcosnorm,listdedocs), reverse = True))
            #print(listdedocs)
            final_index=[]            
            for ele in listdedocs:
                final_index.append(ele+1) #pr faire correspondre l'index
            print("Index mail par ordre décroissant de pertinence : "+str(final_index))
            return final_index
        # Traitement de l'exception en cas d'absence du resultat
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