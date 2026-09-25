e = ["english:"]
m = ["malayalam:"]
h = ["hindi:"]
print("available catagaries")
print(e,m,h)
b=input("enter a catagory to donate:")
c=input("enter a book name:")
print(b)
if b=="english":
    e.append(b)
    print(e)
elif b=="malayalam":
     m.append(b)
     print(m)
elif b=="hindi":
     h.append(b)
     print(h)
else:
     print("other catagory")    

  

