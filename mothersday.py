from arrangement import Arrangement
class MothersDay(Arrangement): 
    def __init__(self): 
        super().__init__()
    def enhance(self, flower): 
        if(flower.stem_length == 4 and flower.organic == True): 
            # referring to the getter in arrangement.py
            self.flowers.append(flower) 
        else: 
            print(f"The flower does not meet Mothers Day requirements.")