try:        

    a=int(input("enter a number"))
    b=int(input("enter a number"))
    print(a/b)



except ZeroDivisionError:
    print("zero cannot be accepted")
except ValueError:
    print("enter a number")