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

"""
# Type() function

number = 100
name = "Rajesh"
price = 99.9
status = True

print(type(number))
print(type(name))
print(type(price))
print(type(status))

class Student:
    pass

s = Student()

print(type(s))

# dir() function

print(dir(s))

# isinstance() function

class Student:
    pass

class Employee(Student):
    pass

s = Student()

print(isinstance(s , Student))
print(isinstance(s , Employee))

# help() function
"""

'''
class Student:
    """
    Student Class
    Used to student information
    """

    def study(self):
        """ Study Student Method"""
        pass


help(Student)
'''

'''
# E-commerce System

class Product:

    def __init__(self , product_id , name , price):

        self.product_id = product_id
        self.name = name
        self.__price = price

    # get method

    def get_price(self):
        return self.__price

    # set method

    def set_price(self , price):

        if price > 0:
            self.__price = price
            print("Price Updated Successfully!.")
        else:
            print("Invalid Price")


    def display(self):
        print("======== Product Details =======")
        print("Product Id : " , self.product_id)
        print("Product Name : " , self.name)
        print("Product Price : " , self.__price)

#child class
            
class Mobile(Product):

    def __init__(self , product_id , name  , price , brand , ram , storage):
        super().__init__(product_id , name , price)

        self.brand = brand
        self.ram = ram
        self.storage = storage

    def display(self):

        super().display()
        
        print("Product Brand : " , self.brand)
        print("Product RAM : " , self.ram)
        print("Product Storage : " , self.storage)

    def buy(self):
        print("Order Placed Successfully!.")
        print("Thank You for Shopping with Us.")

# main function

mobile = Mobile(101 , "iphone 17" , 85000 , "Apple" , 16 , 256 )

while True:

    print("========== E-Commerce Menu =========")

    print("1. View Product")
    print("2. Check Price")
    print("3. Update Price")
    print("4. Buy Product")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        
        mobile.display()

    elif choice == 2:

        print("Current Price : \u20B9" , mobile.get_price())

    elif choice == 3:

        new_price = float(input("Enter new price. : "))

        mobile.set_price(new_price)

    elif choice == 4:

        mobile.buy()

    elif choice == 5:

        print("Thank You!!!!.")
        break

    else:

        print("Invalid Choice")

'''

# Polymorphism

# Polymorphism mean 'one name , many forms.'

# Overloading Method

# Overriding Method

# Method Overloading mean Having multiple method with the same name but diffrent parameters.
'''
class Calculator:

    def add(self , a , b=0 , c=0):
        return a + b +c

c = Calculator()

print(c.add(10 , 20))
print(c.add(10 , 20 , 30))
'''

"""
# *args

class Calculator:

    def add(self , *number):
        return sum(number)

c1 = Calculator()

print(c1.add(10 , 20))
print(c1.add(10 , 20 , 30))
print(c1.add(10 , 20 , 30 , 40))

"""

# Overriding Method

# Method of overriding occurs when a child class provides its own implementation of a method already defined in the parent class.

"""
class Animal:

    def sound(self):
        print("Animal makes sound.")

class Dog(Animal):

    def sound(self):
        # super().sound()
        Animal.sound(self)
        print("Bhow , Bhow")

d = Dog()

d.sound()

class Employee:

    def work(self):
        print("Employee is working.")

class Developer:

    def work(self):
        print("Developer is working on code.")

class Designer:

    def work(self):
           print("Designer is working on Design.")

employee = [Employee() , Developer() , Designer()]

for employ in employee:
    employ.work()

# issubclass()

# issubclass(childclass , parentclass)

class Employee:

    def work(self):
        print("Employee is working.")

class Developer(Employee):

    def work(self):
        print("Developer is working on code.")

class Designer(Employee , Developer):

    def work(self):
           print("Designer is working on Design.")

employee = [Employee() , Developer() , Designer()]

for employ in employee:
    employ.work()

print(issubclass(Employee , Developer))
print(issubclass(Designer  , Employee))
print(issubclass(Designer , Developer))


# Child inherits from both parent and mother

# super()

# super() is used to access parent class methods or constructor from the child class.
"""

# Abstraction

# Abstraction mean Hiding Implementation details and showing only important features.

from abc import ABC , abstractmethod
import math

'''
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car starting!!!!........")


class Bike(Vehicle):

    def start(self):
        print("Bike starting......!!!!!")

c = Car()
b = Bike()

c.start()
b.start()
'''

"""
print("=========== Q.1 =============")

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):

    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

try:

    s = Shape()
except TypeError as e:
    print("Shape Error : " , e)

r = Rectangle(10 , 20)

print("Rectangle Area : " , r.area())


c = Circle(7)

print(f"Circle Area : {c.area():.3f} " , )

print(f"Circle Area : " , round(c.area() , 2) )

"""







    





    













