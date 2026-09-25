class fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __str__(self):
        return f"(self.n)/(self.d)"

    def  __add__(self,other):
        result_num=(self.n*other.d)+(self.n*other.d)
        result_den=(self.d*other.d)
        return f"{result_num}/{result_den}"

    def __sub__(self,other):
        result_num=(self.n*other.d)-(self.n*other.d)
        result_den=(self.d*other.d)
        return f"{result_num}/{result_den}"

    def __mul__(self,other):
        result_num=(self.n*other.d)*(self.n*other.d)
        result_den=(self.d*other.d)
        return f"{result_num}/{result_den}"



obj=fraction(34,3)
obj2=fraction(23,4)

print(obj + obj2)
print(obj -obj2)
print(obj * obj2)