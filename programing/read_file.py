from sys import argv

script,filename ,filename2=argv

file = open(filename)
file2= open(filename2)
print(file.read())
print(file2.read())
file.close()
file2.close()