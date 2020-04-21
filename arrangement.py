class Arrangement: 
    def __init__(self):
        self.__flowers = []

    def enhance(self, flower):
        self.__flowers.append(flower)
        # using setter and getter so that user cannot directly edit flowers
    @property 
    def flowers(self): 
        return self.__flowers
    @flowers.setter
    def flowers(self, new_flowers): 
        self.__flowers = new_flowers
    