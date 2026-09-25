password = input("enter your password: ")

#print(len(password))
#print(password.isalpha())
#print(password.isdigit())
#print(password.islower())
#print(password.isupper())
# iam going to check whether the password contains 8 letters
def letters():
    if len(password) >= 8:
        print("the password contains 8 letters")
    else:
        print("your password doesn't contain 8 letters")


def alpha_caps():
    found = False
    for character in password:
        if character.isupper():
            found = True
            break
    if found:
        print("The password contains a capital letter.")
        return True
    else:
        print("The password doesn't contain a capital letter.")
        return False


def alpha_lower():
    found = False
    for character in password:
        if character.islower():
            found = True
            break
    if found:
        print("The password contains a lowercase letter.")
        return True
    else:
        print("The password doesn't contain a lowercase letter.")
        return False


def digits():
    found = False
    for character in password:
        if character.isdigit():
            found = True
            break
    if found:
        print("The password contains digits.")
        return True
    else:
        print("The password doesn't contain digits.")
        return False


def special_character():
    key = "!@#&?"
    found = False
    for character in password:
        if character in key:
            found = True
            break
    if found:
        print("The password contains special characters.")
        return True
    else:
        print("The password doesn't contain special characters.")
        return False

letters()
alpha_caps()
alpha_lower()
digits()
special_character()
