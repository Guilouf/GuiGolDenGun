 #-*- coding: utf8 -*-

from tfidf import TfIdf
import nltk
import pickle

class Recherche:
    
    def __init__(self):
        #ti = TfIdf()
        #dicoInvNONUTILISE, self.norme = ti.calcul() #retourne un tuple..
        with open("dicotfidf", 'rb') as dicoPKL:
            self.dicoInv= pickle.load(dicoPKL)
        with open("norme", 'rb') as normePKL:
            self.norme= pickle.load(normePKL)
    
    def traitement_requete(self,requete):
        #en gros faut faire la mm chose que pour les docs.. et considérer la requete comme un doc?
        dicoreq =  {}
        listmotreq = nltk.word_tokenize(requete)
        #bon on passe pr l'instant les stopwords, regexp et lower...
        
        #on ne calcule que le tf, car idf = log( nbdedocuments / nbdedocu_contenantle_mot ) = log(1/1) = 0
        #a moins qu'on ne prenne en compte le corpus ds le nb de docs?
        """
        vérifier que le mot soit ds le grand dico...
        """
        for mot in listmotreq:
            if mot not in dicoreq:
                dicoreq[mot] = float( 1 / len(listmotreq) )
            else:
                dicoreq[mot] += float( 1 / len(listmotreq) )
        
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
            if motreq in self.dicoInv: #au cas ou un mot n'est pas dans le corpus
                dicoinvSimpl[motreq] = self.dicoInv[motreq]
                
                for indextuple in range(1, len(dicoinvSimpl[motreq]) ): #sert a creer la liste de docs
                    tutuple = (dicoinvSimpl[motreq])[indextuple]
                    #print(tutuple)
                    
                    if tutuple[0] not in listdedocs:
                        listdedocs.append(tutuple[0])
        
        listdedocs = sorted(listdedocs) #faire gaffe à ca, nrmlt c'est bon
        """
        print("putainnnnnnn")
        print(listdedocs)
        print(dicoinvSimpl)
        """
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
        
        #normalisation des cos
        for cos in listcos:
            cosnorm = float( cos / self.norme )
            listcosnorm.append(cosnorm)
        
        print("resultatfinal")
        print(listdedocs)
        print(listcosnorm)
        print(sorted(listcosnorm, reverse=True))
        

re = Recherche()
dicoreq = re.traitement_requete("aix-marseille mcf adn biologie stage email") #tarragona spain genomes biology biologie
#c'est normal qu'il y ai des problèmes, ya des documents qui manquent (le 93) du ca decale.
rech = re.rech(dicoreq)
print(dicoreq)