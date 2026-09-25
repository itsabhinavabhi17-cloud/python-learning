class parent:
    def __init__(self):
        self.name ="xebec"
        self.league = "onepiece"
        print("the name of the character is " ,self.name, "the name of the league is",self.league)

class child(parent):
    def __init__(self,sign):
        super().__init__()
        self.sign=sign
        print("the character is ",self.sign)

obj=child("worst")