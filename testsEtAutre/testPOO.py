import os
import psutil

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
        
    
        
        
t = TestPOO()      
t.bombe() 
process = psutil.Process()
print(process.memory_info().rss / 1048576 )
print(process.cpu_times())