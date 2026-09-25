from sys import argv


script, filename = argv
file = open(filename)
print("available options are:\n 1.read the file\n 2.write the file\n 3.edit the file")
choice = input("enter your choice")



  