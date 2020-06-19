cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #sorting using the general sort method(alphabetical) - permanent change
print(cars)
cars.sort(reverse=True) #sort the list in the reverse order (alphabetical) - permanent change
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars), "Sorted list") #using sorted() to create a temporary sorted list (only works in print)
print(cars, "Original list")
cars.reverse()#sort the list as it is in reverse(non - alphabetical) - permanent change
print(cars)
print(len(cars))