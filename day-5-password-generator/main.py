#fruits = ["apple", "banana", "orange"]
#for fruit in fruits:
    #print(fruit)

#for i in range(5):
    #print("Hello")
    #print(i)

import random
letters = ["a", "b", "c", "d", "e"]
nr_letters = int(input("How many letters would you like? "))


password = []

for i in range(nr_letters):
    password.append(random.choice(letters))

symbols = ["@", "#", "$", "%", "&", "*"]
nr_symbols = int(input("How many symbols would you like? "))

for i in range(nr_symbols):
    password.append(random.choice(symbols))
    
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
nr_numbers = int(input("How many numbers would you like? "))

for i in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
final_password = "".join(password) #"" → what should go BETWEEN the items? and .join() → join them
print("Your password is: " , final_password)
