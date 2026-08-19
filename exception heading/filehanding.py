'''
with open("demo.txt", "r") as file:
    context = file.read()
    print(context)
'''

print("=======================================")
print("Q-1")
print("=======================================")
"""
try:
    a = float(input("Enter a value : "))
    b = float(input("Enter b value : "))
    result = a / b
    print("Result: ",result)


except ZeroDivisionError as e:
    print("Error",e)
"""

print("=====================================")
print("Q-2")
print("=====================================")

"""
try:
    numbers = [10, 20 ,30 , 40 , 50]

    print("List: ",numbers)

    index = int(input("Enter index value : "))

    print("index number : ",numbers[index])
except ValueError as e:
    print("Error :", e)
except IndexError as e:
    print("Error :", e)
"""

print("=====================================")
print("Q-3")
print("=====================================")
"""
try:
    filename = input("Enter file name : ")
    file = open(filename, "r")
    content = file.read()
except FileNotFoundError as e:
    print("Error:", e)
except OSError as e:
    print("Error:", e)
except PermissionError as e:
    print("Error:", e)
else:
    print("File content : ",content)
    file.close()
"""

print("=====================================")
print("Q-4")
print("=====================================")

"""
try:
    string = ["Shrey" , "pal", "vatsal", "nihar"]

    print("String List: ",string)

    index = int(input("Enter index value : "))
except ValueError as e:
    print("Error :", e)
except IndexError as e:
    print("Error :", e)
else:
    print("index number : ",string[index])
"""

print("=====================================")
print("Q-5")
print("=====================================")

"""
try:
    filename = input("Enter file name : ")
    file = open(filename, "r")
    content = file.read()
except FileNotFoundError as e:
    print("Error:", e)
except OSError as e:
    print("Error:", e)
except PermissionError as e:
    print("Error:", e)
finally:
    if filename is not None:
        print("Context", content)
        file.close()
    print("File closed successfully")
"""

print("=====================================")
print("Q-6")
print("=====================================")

"""
try:
    a = int(input("Enter a Value: "))
    b = int(input("Enter b Value: "))

    result = a / b

    print("Result", result)
    if result < 0:
        raise ValueError("Enter Positive Number.")
except ValueError as e:
    print("Error:", e)
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("End..............")
"""

print("="*40)
print("Q-7")
print("="*40)

"""
try:
    number = int(input("Enter square Number : "))

    if number < 0:
        raise ValueError("Enter Positive Number.")

    square = number ** 2
    print(f"Square of {number} is {square} ")
except ValueError as e:
    print("Error:", e)
"""