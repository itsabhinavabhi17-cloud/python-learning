import math
con = True

def square_root(calcu):
    sr=math.sqrt(calcu)
    return sr

def power_cal(calcu,b):
    pc=math.pow(calcu,b)
    return pc

def fac_cal(calcu):
    fc=math.factorial()
    return fc

def log_cal(calcu):
    lc=math.log(calcu)
    return lc

while con == True:
    def menu():
        print(".......MAIN MENU......")
        print("what do you want to do.")
        print("1.square_root.")
        print("2.power.")
        print("3.factorial")
        print("4.logarithm")


        choice=int(input("enter a choice."))

    
        if choice==1:

            calcu=int(input("enter a input:"))
            print(square_root(calcu))
            

        elif choice==2:
            calcu=int(input("enter a input:"))
            b=int(input("enter the power"))
            print(power_cal(calcu,b))
            

        elif choice==3:
            calcu=int(input("enter a input:"))
            print(fac_cal(calcu))
            
        elif choice==4:
            calcu=int(input("enter a input:"))
            print(log_cal(calcu))
            
        

        else:
            print("invalid option")
    break

menu()
