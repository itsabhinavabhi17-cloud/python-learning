std = {}


def student_details():
    name = input("enter the student name:")
    age = int(input("enter the student age:"))
    mark = int(input("ente the student mark:"))

    std[name] = {
        "age": age,
        "mark": mark
    }

    print("succesfully addedstuden detailes!")

def display_deatiles():
    if not std:
        print("no details found")
        return

    print("\n.....Student Details.....")

    for name,details in std.items():
        print("name:",name)
        print("age:",details["age"])
        print("mark",details["mark"])


def menu():
    while True:
        print("\n......student database")
        print("1.add  student")
        print("2.display details")
        print("3.exit")

        choice=int(input("choose a choise"))

        if choice==1:
              student_details()

        elif choice==2:
            display_deatiles()

        else:
            print("Thank you for your services!")

        break

menu()