# math and random module in python

import math
import random

"""
names = ["rahul" , "amit" , "priya" , "vivek"]

upper_case = [name[0].upper() + name[1:-1] + name[-1].upper() for name in names]

print(upper_case)
"""

"""
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x : x* 2 , numbers))

print(result)
"""

from functools import reduce

number = [10, 20 , 30, 40, 50, 50]

result = reduce(lambda x , y: x * y , number)

print(result)

word = ["python" , "java" , "Javascript", "HTML", "Programming"]

long_word = reduce(lambda x, y : x if len(x) > len(y) else y , word)

print(long_word)

numbers = [10, 15, 20, 25, 30, 35, 40, 45]

even_num = list(filter(lambda x : x % 2 == 0 , numbers))

print(even_num)

