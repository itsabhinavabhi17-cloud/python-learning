try:
    a=int(input("enter a number" ))
    b=int(input("enter a number"))

    def add_numbers():
        print(a + b)

    def substraction():
        print(a-b)

    def division():
        print(a/b)
    def multi():
        print(a*b)

    add_numbers()
    substraction()
    division()
    multi()

except ZeroDivisionError:
    print("a number cannot be divided by zero")

except ValueError:
    print("type a integer")

except TypeError:
    print("integer and string cannot be possible")

except NameError:
    print("we cannot have variable like that")
    

    