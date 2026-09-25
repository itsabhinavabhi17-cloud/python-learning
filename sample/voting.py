#creating a voting machine 

voting_machine= {

    1:0,
    2:0,
    3:0
}

def members():
    print("\n.....welcome to the voting machine.")
    print("your candinates are:")
    print("1.monkey .d .luffy.")
    print("2.kurosaki ichigo.")
    print("3.uzumaki naruto.")

def add_vote():
    print("Choose your candinate.")

    option = int(input("Choose an option."))
    if option in voting_machine:
        voting_machine[option] =voting_machine[option]+1
    else:
        voting_machine[option]=0

        if voting_machine[option]==5:
            print("the candinate wins")

def menu():
    while True:
        print("\n......MAIN MENU.......")
        print("1.vote ")
        print("2.candinates list")
        print("3.none")

        choise=int(input("choose your option."))

        if choise==1:
            add_vote()
        elif choise==2:
            members()

        elif choise ==3:

            print("youre vote has been added")
            break
        else:
            print("invalid option")


def find_winner():
    highest_votes = 5
    winner = None

    for members, add_vote in voting_machine.items():

        if add_vote > highest_votes:
            highest_votes = add_vote
            winner = members

    print("Winner:", winner)
    print("Votes:", highest_votes)
        

menu()    