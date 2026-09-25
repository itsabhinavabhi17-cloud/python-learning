def student_report():
    # get the name of the student
    name = input("enter the name of the student:")
    stdn = int(input("enter the number of subject:"))

    marks = []

    for i in range(stdn):
        mark = int(input(f"enter the mark{i+1}:"))
        marks.append(mark)

    total = sum(marks)
    average = total / stdn 
    highest = max (marks)
    lowest = min (marks)

    if average>=90:
        print("A+:very good")  
    elif average>=80:
        print("A:Good") 
    elif average >=70:
        print("B:average")
    elif average>=60:
        print("C:okay,need to improve!")
    elif average>=50:
        print("D:just pass!")
    else:
        print("youre failed!keep working.")

    print("\n.....student report card....")
    print("student name:",name)
    print("marks       :",marks)
    print("total        :",total)
    print("average      :",average)
    print("highest mark :",highest)
    print("lowest mark  :",lowest)


student_report()