shopping_cart = {"mango":{"price":120 ,"unit":"1kg"},
"orange":{"price":100,"unit":"1kg"},
"apple":{"price":130,"unit":"1kg"},
"chips":{"price":80,"unit":"1 packet"},
"popcorn":{"price":85,"unit":"150 ml"}
}

cart = {}

def display_products():
    for item, info in shopping_cart.items():
        print(item, "=", info["price"], info["unit"])


def adding_items():
    item=input("enter the product")
    quantity=int(input("enter the quantity"))

    if item in shopping_cart:
        cart[item]= quantity
        print("product added")

    else:
        print("product not available")


def removing_items():
    item=input("enter the item you want to remove")

    if item in cart:
        del cart[item]
        print("the selected item is removed")

    else:
        print("the item is not selected")

def display_cart():
    for item, quantity in cart.items():
        print(item, "Quantity:", quantity)

def calculate_bill():
    total = 0

    for item, quantity in cart.items():
        price = shopping_cart[item]
        total = total + (price * quantity)

    print("Total bill:", total)


def menu():
    while True:
        print("\n--- SHOPPING CART ---")
        print("1. Display products")
        print("2. Add product")
        print("3. Remove product")
        print("4. Display cart")
        print("5. Calculate bill")
        print("6. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            display_products()
        elif choice == 2:
            adding_items()
        elif choice == 3:
            removing_items()
        elif choice == 4:
            display_cart()
        elif choice == 5:
            calculate_bill()
        elif choice == 6:
            print("Thank you!")
            break
        else:
            print("Invalid option.")

menu()