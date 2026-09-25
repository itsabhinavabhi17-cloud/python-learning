# create a mapping of state of abbreviation
states ={
    'oregon' : 'OR',
    'florida': 'FL',
    'california':'CA',
    'new york' : 'NY',
    'michigan' : 'MI'
    }
#create a basic set of states and some cities in them

cities = {
    'CA':'San Francisco',
    'MI': 'Detroit',
    'FL':'Jacksonville'
}

#add more cities
cities['NY'] = 'New york'
cities['OR'] = 'Portland'

#print out some cities
print('_' * 10)
print("NY state has:",cities ['NY'])
print("OR state has:",cities['OR'])

#print some states 
print('_' * 10)
print("michigan's abbreviation is:",states['michigan'])
print("floridas's abbreviation is:",states['florida'])


#Print every state abbreviation
print('_' * 10)
for state,abbrev in list (states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state 
print('_' * 10)
for state,city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('_' * 10)
for state ,abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('_'* 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')
if not state:

    print("sorry,no texas.")
                         
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")