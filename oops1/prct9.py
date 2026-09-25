class parent:
    def __init__(self,name,age,occupation):
        self.name =name
        self.age=age
        self.occupation=occupation
        print(self.name)
        print(self.age)
        print(self.occupation)

class sudhi(parent):
    def __init__(self,name,age,occupation,height):
        super().__init__(name,age,occupation)
        self.height=height
        print(self.height)

class norman(parent):
    def __init__(self,name,age,occupation,salary):
        super().__init__(name,age,occupation)
        self.salary=salary
        print(self.salary)

class goblin(parent):
    def __init__(self,name,age,occupation,power):
        super().__init__(name,age,occupation)
        self.power=power
        print(self.power)
#obj=sudhi("agan",21,"piolet",54)
#obj2=norman("harry",32,"nothing",2453)
obj3=goblin("osborn",45,"bussiness man","manipulation")