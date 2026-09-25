def student_details():
    student={}

    student["name"] =input("enter your name:")
    student["age"]=int(input("enter your age:"))
    student["mark"]=int(input("enter your mark:"))
    student["course"]=input("enter your course")
    print("\nStudent Details:")
    for key, value in student.items():
        print(key, ":", value)

# Call the function
student_details()