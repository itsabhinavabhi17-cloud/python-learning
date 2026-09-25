print("insert the atm")
pin = int(input("enter the pin"))
def menu():
    balance = 10000

    while True:
        print("\n....ATM MENU.....")
        print("1.balance")
        print("2.withdraw")
        print("3.deposit")
        print("4.change atm pin")

        option =int(input("please choose a option"))

        if option==1:
            print("youre balance is currently at 10000")
        elif option==2:
             withdraw=int(input("enter the amount you want to withdraw."))
             if balance >=withdraw:
                 print("withdravwl succesful..")
                 print(f"youre current balance{balance-withdraw}")
             else:
                 print("insufficent balance.")
        elif option ==3:
            deposit=input("enter the amount the to deposit.")
            print(f"balnace after deposit{balance+deposit}")
        elif option==4:

            print("1.enter youre current atm pin.")
            print("2.forgot password.")
            
        else:
            print("sorry...better luck next time!")

menu()

        