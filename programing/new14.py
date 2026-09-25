hair =['brown','black','blonde']
thick =['long','short','less']
weights = [1,2,3,4]

for hair in hair:
    print(f"the hair colours are:{hair}")

for thick in thick:
    print(f"the thickness pf hair is :{thick}")

# also we can go through mixed lists too
for i in weights:
    print(f"I got {i}")

elements =[]

for i in range(0,6):
    print(f"adding {i} to the list")
    elements.append(i)

for i in elements:
    print(f"elements in :{i}")