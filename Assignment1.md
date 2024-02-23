# Assignment 1 - Exercise 1
Create a variable called Name
>>> Name = "JUNE LAI"
>>> print (Name)
JUNE LAI
Length of variable Name
>>> Name = "JUNE LAI"
>>> print(len(Name))
8
>>> Name = "JUNE LAI"
>>> first_name, last_name = Name.split()
>>> print(first_name)
JUNE
>>> print(last_name)
LAI
# Assignment 1 - Exercise 2
>>> fruits = []
>>> print(fruits)
[]
>>> fruits = ['apple' , 'orange' , 'lemon' , 'banana' ,'grapes']
>>> print(fruits)
['apple', 'orange', 'lemon', 'banana', 'grapes']
>>> fruits.append('strawberry')
>>> print(fruits)
['apple', 'orange', 'lemon', 'banana', 'grapes', 'strawberry']
>>> fruits.sort()
>>> print(fruits)
['apple', 'banana', 'grapes', 'lemon', 'orange', 'strawberry']
>>> fruits_reverse = list(fruits)
>>> print(fruits_reverse)
['apple', 'banana', 'grapes', 'lemon', 'orange', 'strawberry']
>>> fruits_reverse.reverse()
>>> print(fruits_reverse)
['strawberry', 'orange', 'lemon', 'grapes', 'banana', 'apple']
Dictionary
>>> inventory = {}
>>> print(inventory)
{}
>>> inventory['first_name']='June'
>>> inventory['last_name']='Lai'
>>> print(inventory)
{'first_name': 'June', 'last_name': 'Lai'}
>>> fruits = ['apple','orange','lemon','grapes','banana']
>>> fruits = ["apple","orange","banana","lemon","grapes"]
>>> print(fruits)
['apple', 'orange', 'banana', 'lemon', 'grapes']
>>> fruits.sort()
>>> print(fruits)
['apple', 'banana', 'grapes', 'lemon', 'orange']
>>> inventory['fruits']=list(fruits)
>>> print(inventory)
{'first_name': 'June', 'last_name': 'Lai', 'fruits': ['apple', 'banana', 'grapes', 'lemon', 'orange']}
>>> len(inventory['fruits'])
5
>>> inventory['fruits_count'] = len(inventory['fruits'])
>>> print(inventory)
{'first_name': 'June', 'last_name': 'Lai', 'fruits': ['apple', 'banana', 'grapes', 'lemon', 'orange'], 'fruits_count': 5}
>>> inventory
{'first_name': 'June', 'last_name': 'Lai', 'fruits': ['apple', 'banana', 'grapes', 'lemon', 'orange'], 'fruits_count': 5}
>>> inventory['fruits_count']+=1
>>> inventory['fruits'].append('mango')
>>> print(inventory['fruits'])
['apple', 'banana', 'grapes', 'lemon', 'orange', 'mango']
>>> print(inventory)
{'first_name': 'June', 'last_name': 'Lai', 'fruits': ['apple', 'banana', 'grapes', 'lemon', 'orange', 'mango'], 'fruits_count': 6}
# Assignment 1 - Exercise 4
>>> print("I am thinking of a number between 1 to 20.")
I am thinking of a number between 1 to 20.
>>> import random
>>> secret_number = random.randint(1,20)
>>> print(f"Test: the secret number is:{secret_number}")
Test: the secret number is:6

>>> print("Take a guess")
Take a guess
>>> guess = int(input())
>>> if guess > secret_number:
... print("Your guess is too high.")
>>> elife guess< secret_number:
>>> print("Your guess is too low.")

>>> if guess == secret_number:
... print("Good job! You guessed my number in guesses!")
>>> else:
>>> print("Nope. The number I was thinking of was " + secret_numberif guess == secret_number")

>>> import random
>>> secret_number = random.randint(1,20)
>>> print(f"Test: the secret number is:{secret_number}")
Test: the secret number is:6
>>> print("Take a guess")
Take a guess
>>> guess = int(input())
>>> if guess > secret_number:
... print("Your guess is too high.")
>>> elife guess< secret_number:
>>> print("Yrour guess is too low.")
>>> if guess == secret_number:
... print("Good job! You guessed my number in guesses!")
>>> else:
>>> print("Nope. The number I was thinking of was " + secret_numberif guess == secret_number:
>>> print("Good job! You guessed my number in guesses!")
Good job! You guessed my number in guesses!


>>> import random
>>> print("I am thinking of a number betweet 1 to  20.")
I am thinking of a number betweet 1 to  20.
>>> secret_number = random.randint(1,20)
>>> for i in range(1,7):
    print("Take a guess")
>>> guess = int(input())

if guess > secret_number:
>>> print("Your guess is too high.")
Your guess is too high.
    elif guess < secret_number
>>> print("Your guess is too low.")
    else:
>>> break

>>> if guess == secret_number:
    print(f"Good job! You guessed my number in (i) guesses!")
    else:
>>> print("Nope. The number i was thinking of was " + str(secret_number))

# Assignment 1 - Exercise 3
choice = "sunny"
textcontent = ""

if choice == "sunny":
    textcontent = "It is nice and sunny outside today. Wear Short!Go to the beach, or the park, and get an ice cream."
elif choice ="rainy":
    textcontent = "Rain is falling outside; take a rain coat and an umbrella, and don't stay out for too long."
elif choice ="snowing":
    textcontent = "The snow is coming down - it is freezing! Best to stay in with a cup of hot chocolate, or go build a snowman."
elif choice = "overcase":
    textcontent = "It isn't raining, but the sky is grey and gloomy; it could turn  any minute, so take a rain coat just in case."
else:
    textcontent = ""

print(choice)
print(textcontent)

# Assignment 1 - Exercise 5
class Circle:
    pi=3.14159

    def __init(self,radius):
        self.radius = radius 

    def are(self):
        return self.pi * (self.radius **2)
    
    def circumstance():
        return 0 

class bankaccouny:
    def __init__(self,account_number,owner_name):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = 0
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw {amount}")
        else:
            print(f"Insufficient funds.")

    def display_balance(self):
        print(f"account_number:{self.account_number}")
        print(f"owner_name:{self.owner_name}")
        print(f"balance:{self.balance}")



