# python OOP Example

# Class definition

# A class is a blueprint or template used to create objects.
# It defined what data and actions an object Will hane.obs
# Data : Attributed
# Actions : Methods

# House Blueprint

# Class = Blueprint / Design

# Object defination

# An object is a real instance of a class.

# it contains actual values and can use the method defined in the class.abs

# blueprint => Honda , Audi, Tesla

# Object : Real thing

# Encapsulations

# Encapsulation means keeping data and method together inside a class and protecting important data from direct access.

# ATM Machine => Withdraw Cash => Deposit Case

# Encapsulation = Data Protection + Controlled acess

"""

class ClassName:
    pass

cae = ClassName()

"""

"""

1. Attributes
2. Constructor
3. Destructor
4. self keyword

"""
'''
class Car:

    # Contsructor 
    
    def __init__(self , brand=None , model=None , color=None , price=None , name=None , age=None, dob=None, marks=None):

        #Car

        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

        #User

        self.name = name
        self.age = age
        self.dob = dob
        self.marks = marks

    # Method
    def start(self):
        print(f"{self.brand} {self.model} is Stating.......")

    # Method

    def Car_Details(self):
        print(f"""
Brand : {self.brand}
Model : {self.model}
Color : {self.color}
Price : {self.price}
        """)

    def User_Details(self):
        print(f"""
Name : {self.name}
Age : {self.age}
DOB : {self.dob}
Marks : {self.marks}
        """)

car1 = Car("Honda" , "Amaza" , "Black" , 10000 , "Shrey" , 25, "01-01-2000" , 85)

car1.Car_Details()

car1.User_Details()

'''

'''
class Student:

  # contsructor

  def __init__(self , name=None , age=None , dob=None , marks=None):

    #user
    self.name = name
    self.age = age
    self.dob = dob
    self.marks = marks
   

  def User_Details(self):
    print(f"""
Name : {self.name}
Age : {self.age}
DOB : {self.dob}
Marks : {self.marks}
    """)

student1 = Student("Shrey" , 25 , "01-01-2005", 100)

student1.User_Details()

# Simple Creation

class Person:
    pass

p1 = Person()

print(type(p1))

class Person:
    # Attribute
    name = "Shrey"

    age = 25

    course = "Python"

p1 = Person()

print(p1.name)
print(p1.age)
print(p1.course)

'''

'''
# class Student:

class Student:

    def __init__(self):
        self.name = "vivek"
        self.age = 20
    
    def display(self):
        print(f"Welcome to Python OOP")

s1 = Student()

s1.display()
s1.name = "Rahul"
print(s1.name)
print(s1.age)

'''

'''
# Bank Account App

class BankAccount:

    def __init__(self , name , __balance):
        self.name = name
        self.__balance = __balance

    def deposite(self , amount):
        if amount >= 1:
            self.__balance += amount
            print(f"{self.name} deposite Sucessfully.")
        else:
            print("Enter Positive Number!")
            return

    def Withdraw(self , amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.name}Withdraw Sucessfully")
        else:
            print("insufficient balance!")
            return

    def display(self):
        print(f"{self.name} Current account balance : {float(self.__balance)}")


name = input("Enter Your name : ")
balance = int(input("Enter Opening balance : "))

account = BankAccount(name, balance)

while True:
    print("""
1. Display amount
2. Deposit amount
3.Withdraw amount
4. Exit
""")

    choice = int(input("Select Your choice : "))

    match choice:
        case 1:
            account.display()
        case 2:
            deposite = int(input("Enter Deposite amount : "))
            account.deposite(deposite)
        case 3:
            withdraw = float(input("Enter Withdraw Amount : "))
            account.Withdraw(withdraw)
        case 4:
            print("Thank you . Visiting again!")
            break
        case _:
            print("Enter 1 to 4 choice Only.")

'''

# Multiple Objects with Destructor
'''
class Customer:

  def __init__(self , name):
    self.name = name
    print(f"{self.name} logged in.")

  def shopping(self):
    print(f"{self.name} is shopping.")

  def __del__(self):
    print(f"{self.name} logged out.")

c1 = Customer("Rahul")
c2 = Customer("Priya")
c3 = Customer("Ronak")

c1.shopping()
c2.shopping()
c3.shopping()

del c1
del c2
del c3
'''
# Default Constructor  , Destructor
'''
class Employee:

  def __init__(self):
    self.name = "vivek"
    self.department = "IT"

    print(self.name , "joined office.")

  def display(self):
    print("Employee :" , self.name)
    print("Department : " , self.department)

  def __del__(self):
    print(self.name , "Left Office.")


emp = Employee()

emp.display()

del emp
'''
# Bank Account

'''
class BankAccount:

  def __init__(self , account_holder , account_number , balance):
    self.account_holder = account_holder
    self.account_number = account_number
    self.balance = balance # Private Variable

  def deposit(self , amount):

    if amount > 0:
      self.balance += amount
      print(f"${amount} Deposited Successfully!.")

    else:
      print("Invalid amount.")


  def withdraw(self , amount):

    if amount <= 0:
      print("Invalid amount.")

    elif amount > self.balance:
      print("Insufficient amount.")

    else:
      self.balance -= amount
      print(f"${amount} withdraw Successfully!.")

  def check_balance(self):
    print(f"Current Balance : ${self.__balance}")

  def display(self):

    print("======= Account Details =======")

    print("Account Holder : " , self.account_holder)
    print("Account Number : " , self.account_number)
    print("Account Balance : " , self.balance)


name = input("Enter Account Holder Name : ")
acc_num = int(input("Enter Account Number: "))
balance = float(input("Enter Opening amount: "))

account = BankAccount(name , acc_num , balance)

print(account.balance)

while True:

  print("1. Deposit")
  print("2. Withdraw")
  print("3. Check Balance")
  print("4. Display")
  print("5. Exit")

  choice = int(input("Enter your choice : "))

  if choice == 1:

    amount = float(input("Enter deposite amount : "))
    account.deposit(amount)

  elif choice == 2:

    amount = float(input("Enter withdraw amount : "))
    account.withdraw(amount)

  elif choice == 3:
    account.check_balance()

  elif choice == 4:
    account.display()

  elif choice == 5:
    print("Thank You!!!!")
    break

  else:
    print("Invalid Choice")
'''

# Inheritance OOP in Python

# 1. Single Inheritance
'''
class Parent:

  def display(self):
    print("I am Parent Class.")

class Child(Parent):

  def show(self):
    print("I am Child Class.")

c1 = Child()

c1.display()
c1.show()

'''
# Multiple Inheritance
'''
class Teacher:

  def manage(self):
    print("Teaching Students.")

class Admin:

  def manage(self):
    print("Managing School.")

class Headmaster(Admin , Teacher):

  def guide(self):
    print("Guiding Teachers and Students")
    Teacher.manage(self)
    Admin.manage(self)


h1 = Headmaster()

h1.guide()

'''
# Multilevel Inheritance
'''
class Grandparent:

  def role(self):
    print("Grandparent gives values.")

class Parent(Grandparent):

  def responsibility(self):
    print("Parent take care of family.")

class Child(Parent):
  
  def study(self):
    print("child is studying.........")


c1 = Child()

c1.role()
c1.responsibility()
c1.study()

p1 = Parent()

p1.role()
p1.study()

'''
'''
# Hierarchical Inheritance

class Animal:

  def eat(self):
    print("Animal is Eating....")

class Dog(Animal):

  def sound(self):
    print("bhow...bhow...")

class Cat(Animal):

  def sound(self):
    print("Meow....Meow....")


d = Dog()

d.eat()
d.sound()

c = Cat()

c.eat()
c.sound()
'''
# Hybrid Inheritance
"""
class Person:

  def work(self):
    print("Person is working...")


class Teacher(Person):

  def work(self):
    super().work()
    print("Teaching Students")

class Admin(Person):

  def work(self):
    super().work()
    print("Manage School.")


class Headmaster(Teacher , Admin):

  def work(self):
    super().work()
    print("Manage Teacher and Students")


h = Headmaster()

h.work()
"""











    





    













