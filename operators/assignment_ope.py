# 1. Increment and decrement a number
"""
i = 1
print("Increment number")
while i < 6:
    print(i)
    i += 1
print("decrement number")
while i > 0:
    print(i)
    i -= 1
"""

# 2. Use +=, -=, *= in calculations
"""
i = 1
l = 6
u = 1
print("calculation")
while i < 6:
    i += 1
    l -= 1
    u *= 1

print("sum:",i)
print("sum:",l)
print("sum:",u)
"""

# 3. Create running total (add numbers step by step)
"""
total = 0
num = 1

while num <= 5:
    total += num
    print(f"Added: {num} running Total: {total}")
    num += 1

print("Total",total)
"""
# 4. Salary increment calculation
"""
salary = int(input("Enter current salary: "))
increment = int(input("Enter yearly increment: "))
years = int(input("Enter number of years: "))

year = 1

while year <= years:
    salary += increment
    print(f"Year {year} salary {salary}")
    year += 1
"""
# 5. Discount calculation using assignment operators
"""
price = float(input("Enter product price: "))
discount = float(input("Enter discount amount: "))

price -= discount

print("Discount Price =", price)
"""
