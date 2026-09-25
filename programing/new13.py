print("""you enter a dark room with two doors.
do you go through door #1 or #2 ?""")

door = input(">")
if  door =="1":
    print("there's a giant  bear here eating a cheese cake.")
    print("what do you do?")
    print("1.take the cake.")
    print("2.scream at the bear ")
    print("3.or dance infront of the bear")

    bear = input(">")
    if bear == "1":
        print("the bear eats your face off.good job!")
    elif bear== "2":
        print("the bear eats your leg .well done!")
    else:
        print(f"well,doing {bear} is probably better.")
        print("bear runs away")

elif door == "2":
    print("you entered to the shadow monarch domain")
    print("what are you gonna do .")
    print("1.die")
    print("2.or reborn")

    monarch =input(">")
    if monarch == "1" :
        print("youre are born to die")



    elif monarch == "2":
        print("you becomes the monarch of shadow:")
        print("good gob!")

    else:
        print ("you could walk away !")
    
    