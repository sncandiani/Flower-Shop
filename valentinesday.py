from arrangement import Arrangement

class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()
    def enhance(self, flower): 
        if(flower.stem_length == 7 and flower.organic == False): 
            self.flowers.append(flower)
        else: 
            print(f"The flower does not meet Valentines Day requirements.")
    