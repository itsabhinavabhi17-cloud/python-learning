class parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("this is the name",self.name)
        print("thisis the age",self.age)
class child(parent):
    def __init__ (self,name,age,school):
        super().__init__(name,age)
        self.school = school
        print("this is the school of ",self.school)
        
    

student=child("abhi",21,"gss")

