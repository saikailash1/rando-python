#constructing a dictionary
alien_0 = {'color':'yellow','points':5}
print(alien_0)

#accessing elements of a dictionary
print(alien_0['color'])
print(alien_0['points'])
new_point = alien_0['points']
print(f"You have earned {new_point} points!")

#adding new elements
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#you can also start with an empty dictionary
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 10
print(alien_1)

#changing data in the dictionary
print(f"Old color: {alien_1['color']}")
print(alien_1)
alien_1['color'] = 'yellow'
print(f"New color: {alien_1['color']}")
print(alien_1)

#deleting data from the dictionary
del alien_1['points']
print(alien_1)

#get() method to access elements
point_value = alien_1.get('points', 'No point value assigned.')#much like ternary operator
print(point_value)

#looping through dictionary
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key, value in user_0.items(): #use items when accessing both key and value
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in favorite_languages.keys(): # dict.keys() for accessing only keys
    print(name.title())
    #for name in favourite_languages would also give you the same result

#set - collection of non-repetitive elements
for language in set(favorite_languages.values()):
	print(language.title())

##########################NESTED DICTIONARY###############################
# DICTIONARY IN A LisT
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#you can also edit each alien like below
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

#########################################################################
#LIST IN A DICTIONARY
# Store information about a pizza being ordered.
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
"with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
    