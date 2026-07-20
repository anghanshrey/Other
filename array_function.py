# Common Typecodes
'''
arrayIdentifierName = array(typecode , [initilizer])

"i" : "integer"
"f" : "float"
"d" : "double"
"u" :"Unicode Character"

Note: Array cannot store heterogeneous data. if you need diffrent datatype together , use a list

'''

"""
from array  import *

myarray = array('i', [1, 2, 3, 4, 5])

print(myarray)

for i in myarray:
    print(i)
"""

# Using for loop  + append()

# Ask the user how many element they want to enter.
# Create an empty list.
# Use a for loop to take input.
# Store each element using append()

"""
size = int(input("Enter size of array: "))

numbers = []

for i in range(size):
    value = int(input(f"Enter Elements {i + 1} :"))
    numbers.append(value)

print("Array Elements:")

print(numbers)
"""

"""
size = int(input("Enter size of array: "))
value = int(input("Enter Element : "))

numbers = []

for i in range(size):
    numbers.append(value)
    value += 10

print("Array Elements:")

print(numbers)
"""

# Using Map() + Split()

#Ask user to enter all element in one line seperated by space.
# split() convert the input string into a list
# map(int , ...) convert each string into an integer
#list() stores the result as a list.
"""
numbers = list(map(int, input("Enter Array Elements : ").split()))

for i in numbers:
    print(i)

print(numbers)
"""

# Using List Comprehension

"""
size = int(input("Enter Size of array : "))

numbers = [int(input(f"Enter Element {i + 1} :"))]

print("Array Elements:")

print(numbers)
"""
