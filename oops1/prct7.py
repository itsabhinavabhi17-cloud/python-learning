class character:
    def __init__(self):
        self.name="somu"
        self.age = 21
        print("the name of the character is",self.name )
        print("the age of the character is ",self.age)

class devolopment(character):
    def __init__(self,build):
        super().__init__()
        self.build = build
        print("the character is devolomented by ",self.build)
class power(devolopment):
    def __init__(self,build,raw):
        super().__init__(build)
        self.raw=raw
        print("the power of the character is",self.raw)

obj=power("emotion","smash")