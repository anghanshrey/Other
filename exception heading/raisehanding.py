# raise Keyword

# Menually raise an exception
# raise ExceptionType("a clear meassage for explaining what went wrong.")

# assert

# Checks Weather a condition is True.
# assert condition , "message shown if the condition is False."

# Custom Exception

# raise keyword

'''
age = 17

if age < 18:
    raise ValueError("Age must be 18 or above.")
'''

'''
def get_age(age):
    if age < 0:
        raise ValueError("Age must be 18 or above.")
    return age

try:
    print(get_age(5))
except ValueError as e:
    print(f"Error : {e}")
'''

"""
# Assert keyword

marks = 75

assert marks >= 0, "Marks cannot be negative"

def calculate_average(numbers):
    assert len(numbers) > 0 , "list cannot be empty"
    return sum(numbers) / len(numbers)

print(calculate_average([10, 20 , 30]))
print(calculate_average([])) 
"""

# Custom Exception

class InsufficientFundError(Exception):
    """ Raised When a withdrawal exceted the available."""
    pass

class BankAccount:

    def __init__(self, balance = 0):
        self.balance = balance

    def withdraw(self, amount):
        assert amount > 0, "Withdrwal amount must be positive."
        if amount > self.balance:
            raise InsufficientFundError(f"Cannot withdraw {amount} balance is only {self.balance} ")
        self.balance -= amount
        return self.balance

account = BankAccount(1000)

try:
    account.withdraw(1000)
    account.withdraw(100)
except InsufficientFundError as e:
    print(f"transction Error :",e)
