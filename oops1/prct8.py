class vodafone:
    def __init__(self,name,covrage):
        self.name=name
        self.covrage=covrage
        print(self.name)
        print(self.covrage)

class idea:
    def __init__(self,brand):
        self.brand=brand
        print(self.brand)
class airtel(vodafone,idea):
    def __init__(self,name,covrage,brand):
        vodafone.__init__(self,name,covrage)
        idea.__init__(self,brand)

obj=airtel("krish","trivandrum","airtel")