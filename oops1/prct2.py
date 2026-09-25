class Student:

    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def total(self):
        return self.mark1 + self.mark2 + self.mark3

    def average(self):
        return self.total() / 3

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def display(self):
        print("\n----- STUDENT DETAILS -----")
        print("Name:", self.name)
        print("Mark 1:", self.mark1)
        print("Mark 2:", self.mark2)
        print("Mark 3:", self.mark3)
        print("Total:", self.total())
        print("Average:", self.average())
        print("Grade:", self.grade())


name = input("Enter student name: ")
mark1 = float(input("Enter mark 1: "))
mark2 = float(input("Enter mark 2: "))
mark3 = float(input("Enter mark 3: "))

student1 = Student(name, mark1, mark2, mark3)

student1.display()