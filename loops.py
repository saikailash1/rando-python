#for loop
magicians = ['alice', 'david', 'carolina']
for i in magicians:
	print(i)

for value in range(0,5): #last value does not get printed when using range
	print(value+1)

#making list with range function
li = list(range(1,6))
print(li)

#skipping numbers using range
li2 = list(range(2,11,2))
print(li2)

#squares of first 10 numbers
squares = []
for i in range(1,11):
	squares.append(i**2)
print(squares)

#squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#some additional functions
minimum = min(squares)
maximum = max(squares)
total = sum(squares)
print(minimum)
print(maximum)
print(total)

#list comprehension
values = [i**2 for i in range(1,11)]
print(values)