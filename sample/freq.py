sentance = input("enter a sentance:")

word = sentance.split()

count = {}
for word in sentance:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
    

for word,count in count.items():
    print(word,count)





