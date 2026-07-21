# Python Functions

# Bulit-in Functions

print("="*20)
print("Functions with Python")
print("="*20)


numbers = [1, 45, 85, 22, 66, 34]

print(numbers)

print(len(numbers))

print(max(numbers))

print(min(numbers))

print(sorted(numbers))

print(sum(numbers))

print("="*20)
print("UDF Functions")
print("="*20)

def add(a, b):
    print(a + b)

add(10, 20)
add(20, 20)

"""

1. Reusability
2. Cleaner Code
3. Better Organization
4. Reduce Repetition

"""

print("="*20)
print("Recursion")
print("="*20)

# A function calling itself.

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(10))

# Sum of Numbers

def total(n):

    if n == 0:
        return 0

    return n + total(n - 1)

print(total(10))

# Anonymous Function / Lambda Functions

square = lambda x : x * x

print(square(5))

add = lambda a, b: a+ b

print(add(10, 20))

# Arbitray Arguments (*args)

# Write a Python function that accept any number of arguments and return their sum.

def addition(*args):
    total = 0

    for i in args:

        total += i

    print("Total:",total)

addition(10, 20, 30, 40, 50)

# Keyword Arguments (**kwargs)

# Write a Python function that accept student information using keyword arguments and prints all student details.


def student(**kwargs):
    print("Student Details")

    for key , value in kwargs.items():
        print(f"{key} : {value}")

student(name = "vivek", age = 25, city = "surat", course = "Python")

# doc (Documentation String)

# Write a function to calculate the area of a rectangle and display its Documentation.

def rectangle(length , width):
    """
    Function Name : reactangle

    Purpose:
        Calculate rectangle area.

    Parameter:

        length : int
        width : int

    Return:
        Area of rectangle
"""

    return length * width

print("Area :" , rectangle(10 , 20))
print(rectangle.__doc__)

# Lambda with map()

numbers = [10, 15, 20, 25, 30, 35]

result = list(map(lambda x : x ** 2, numbers))

print(result)

# Lambda with filter()

numbers = [10, 15, 20, 25, 30, 35]

even = list(filter(lambda x : x % 2 == 0, numbers))

print(even)

# Lambda With sorted()

students = [("vivek", 85) , ("Rajesh" , 72), ("Amit", 22), ("Raj" , 50)]

print(students)

result = sorted(students , key = lambda x : x[1])

print(result)

# Global Keyword in Python

total = 0

def increment():
    global total
    total += 2

increment()
increment()
increment()
print(total)

# Multiple Return Values

def calculation(a, b, c):

    total = a + b + c
    average = total / 3

    maximum = min(a , b, c)

    minimum = min(a , b, c)

    return total , average , maximum , minimum

total , average , maximum , minimum = calculation(10, 20, 30)

print(total)

# lambda with reduce()

from functools import reduce

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda x , y : x * y , numbers)

print(product)

# Global vs Local Variables

name = "python"

def demo():
    global name
    name = "javascript"

    print(name)

demo()
print(name)

# Return multiple values (student result)

def result(m1 , m2, m3):

    total = m1 + m2 + m3

    percentage = total / 3

    if percentage >= 90:

        grade = "A"

    elif percentage >= 75:

        grade = "B"

    elif percentage >= 60:

        grade = "C"

    else:

        grade = "Fail"

    return total , percentage , grade

total , percentage , grade = result(90, 89, 95)

print(total)
print(percentage)
print(grade)
