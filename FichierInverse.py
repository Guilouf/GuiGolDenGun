 #-*- coding: utf8 -*-
#F9 pour lancer le prog!

#penser ensuite à la serialisation, à voir
import main
import operator #pour laddition des tuples
from main import parsemail

global listeDmail
listeDmail = parsemail()
print("#######################################################")

def fichInv():

    dicoInv = {} #pas sur qu'un dico soit une si bonne idée..
    
    for indexmail in range(len(listeDmail)):#defile les mails
        #print(mess[3])
        
        for mot in (listeDmail[indexmail])[3]:#defile les mots du coprs de mail
            
            if mot not in dicoInv:#premiere fois que le mot est detecté
                #freqmess = 1
                #print("merde") #faut faire un dictionnaire de tuples.. ptetre pas une bonne idée les tuples en fait
                dicoInv[mot] = [[1,0],(indexmail,1)] #frequence totale=> au lieu d'indexmail, faire tuple indexmail + freq dans le mail..
                
            else: #le mot est déja présent dans le dico
                #freqmess = (dicoInv[mot])[1]+1 #ouais mais non...: il faut que cette frequence soit associée à chaque message..
                #dicoInv[mot] = tuple(map(operator.add, dicoInv[mot], (1,freqmess) ))
                ((dicoInv[mot])[0])[0] += 1 #ajout de 1 a liste de frequence totale
                
                if ((dicoInv[mot])[-1])[0] != indexmail:#la premiere occurence du mot dans ce mail ((dicoInv[mot])[-1])[0] = l'index du mail du dernier tuple du mot dans le dico...
                    (dicoInv[mot]).append((indexmail,1))
                else: #prochaine occurences du mot dans le mm mail
                    (dicoInv[mot])[-1] = tuple(map(operator.add, (dicoInv[mot])[-1], (0,1) ))
 
    return dicoInv
dicoInv = fichInv()

           
print("#########              DICO                 #############")    
""    
print(str(dicoInv))

for i in dicoInv:
    print(i +": "+ str(dicoInv[i]))
""