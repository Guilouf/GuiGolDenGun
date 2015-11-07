

class TestPOO:
    
    def __init__(self):
        self.nbdevivants = 150
        self.puissancebombe = 7
        self.message()
        
    def imprimort(self,effetBombe):
        print(effetBombe) 
     
    def message(self):
        print("la guerre!") 
    
    
     
     
    def bombe(self):
        effetBombe = self.nbdevivants * ( 1 / self.puissancebombe)
        self.imprimort(effetBombe)
        return effetBombe
        
    def list
        
        
t = TestPOO()      
t.bombe() 