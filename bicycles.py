bicycles = ['trek', 'cannondale', 'redline', 'specialized']
a = 5
print(bicycles)
print(bicycles[0]) #accessing elements using indexes
print(bicycles[3].title()) #formatting the elements (f-string can also be used)
print(bicycles[-1]) #prints the last element (use '-' symbol to access elements from the last)
print("value of a is:",a)
bicycles.append('hercules') #append method
print(bicycles)
bicycles.insert(2,'BSA') #insert method
print(bicycles)
del bicycles[0] #del using indexes
print(bicycles)
pop = bicycles.pop() #pop - removes last element
print(bicycles)
print(pop)
print(bicycles.pop(0)) #pop using index
bicycles.remove('redline') #removing item by value
print(bicycles)