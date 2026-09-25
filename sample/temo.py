print("\n......welcome to the temparature  program......")




def celcuis_farenheit(celcuis):
    c=(celcuis * 9/5) + 32
    return c

def celcuis_kelvin(celcuis):
    k=celcuis + 273.5
    return k
def kelvin_celcuis(kelvin):
    ck=kelvin-273.15

    return ck
def kelvin_farenheit(kelvin):
    kf=(kelvin-273.15)*9/5+32
    return kf

def farenheit_kelvin(farenheit):

    fk=(farenheit-32)*9/5+273.15
    return fk

def farenheit_celcuis(farenheit):
    cf=(farenheit-32)*5/9
    return cf



def menu():
    print("\n.........WELCOME TO THE MENU........")
    print("1.celcuis to farenheit")
    print("2.celcuis to kelvin ")
    print("3.farenheit to kelvin")
    print("4.farenheit to celcuis")
    print("5.kelvin to celcuis")
    print("6.kelvin to farenheit")

    choice=int(input("choose a choice."))

    if choice==1:
        temperature=float(input("enter a input:"))
        print(celcuis_farenheit(temperature))

    elif choice==2:
        temperature=float(input("enter a input:"))
        print(celcuis_kelvin(temperature))

    elif choice==3:
        temperature=float(input("enter a inpu:t"))
        print(farenheit_kelvin(temperature))
    elif choice==4:
        temperature=float(input("enter a input:"))
        print(farenheit_celcuis(temperature))
    elif choice==5:
        temperature=float(input("enter a input:"))
        print(kelvin_celcuis(temperature))

    elif choice==6:
        temperature=float(input("enter a input:"))
        print(kelvin_farenheit(temperature))
    else:
        print("invalid option")            
menu()