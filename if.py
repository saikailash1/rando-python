#if-else statement
cars = ['bmw', 'audi', 'toyota', 'subaru']
for i in cars:
	if i=='audi':
		print(i.upper())
	else:
		print(i.title())

#not-equal statements
req_topping = "pepperoni"
if req_topping != "olives":
	print("Not the Mushrooms!!!")

age = 21
age2 = 22
#and statement
if age == 21 and age2 == 22:
	print("true")

#or statements
if age == 21 or age2 == 22:
	print("true")

#'in' statement check
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings

#'not in' statements
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(user.title()+", You are not banned.")

#if-elif-else statements
age  = 14
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")