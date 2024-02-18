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