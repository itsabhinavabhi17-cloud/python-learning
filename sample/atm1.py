print("insert your pin")
pin=int(input("enter your pin"))
balance = 10000

def check_balance():
    global balance
    print(f"your {balance} is available now")

#now creating a withdraw method for the atm

def withdraw_amount():
    global balance
    amount=int(input("enter your amount to withdraw"))

    if balance>=amount:
        balance = balance - amount
        print("your withdrawelis successful")
        print(f"your available amount is {balance}")
    else:
        print("insufficent balance")


def deposit():
    global balance
    deposit = int(input("enter the amount to deposit"))

    balance = balance +deposit 
    print("deposit succesful")
    print(f"your available balance {balance}") 

def menu():
    while True:
        print("\n......MAIN MENU......")
        print("1.withdraw.")
        print("2.deposit.")
        print("3.change pin.")
        print("4.check balance.")

        choise =int(input("choose an option"))

        if choise ==1:
           withdraw_amount()

        elif choise == 2:
            deposit()
        elif choise ==3:
            print("enter youre current pin")
            print("forgot youre password")

        elif choise ==4:
           check_balance()

        else:
            ("invalid access")

correct_pin =1234
if correct_pin ==pin:

   print("youre access granted")
   menu()
else:
    print("invalid access")


    