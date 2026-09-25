import random

num=random.randint(1,100)



while True:

    user=int(input("enter a random number:"))
    if num<user:
        print("the guess is too high!")

    elif num>user:
        print("the guess is too low!")

    elif num==user:
        print("yes ;you guess the right answer")
        print("congragulations buddy")
        break
    else:
        print("invalid option")

