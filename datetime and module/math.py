# math and random module in python

import math
import random
"""
number = int(input("Enter a number: "))

print("Square root :", math.sqrt(number))
print("power , 2 :", math.pow(number , 2))
print("Factorial :" , math.factorial(number))           
"""

"""
radius = float(input("Enter radius of the circle:"))

area = math.pi * radius *radius

print("Circle Area :", area)
"""

"""
num = float(input("Enter a number for natural logarithm:"))

if num > 0:
    print(math.log(num))
else:
    print("Natural Logarithm is possible only positive number.")
"""

"""
angle = float(input("Enter a angle in degree:"))

angle_radian = math.pi / 180 * angle

print("sin" , math.sin(angle_radian))
print("cos" , math.cos(angle_radian))
"""

def Absolute(value):

    print("value : ", value)
    print("Ceilling Value : ", math.ceil(value))
    print("Floor Value : ", math.floor(value))
    print("Absolute Value : ", math.fabs(value))
    
value = float(input("Enter a decimal number : "))

Absolute(value)


