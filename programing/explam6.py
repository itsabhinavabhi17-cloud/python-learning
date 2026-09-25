#check a number is positive,zero,negative in lamda function


num =int(input("enter a number:"))
''
chek =lambda x:"zero" if x==0 else  "positive" if x>0 else "negative"
print(chek(num))