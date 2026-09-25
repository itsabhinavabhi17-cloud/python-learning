a= int(input("enter a number:"))
b = int(input("enter a number:"))

max =lambda a,b:a if a>b else b

print(max(a,b))