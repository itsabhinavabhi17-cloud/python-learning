def  substracting(a,b):
    return a.find(b)

a=input("enter the sentence")
b=input("enter the sentence to substract")

i = substracting(a,b)

if i==-1:
    print("the values not defined:")

else:
    print("the values has founded in index")