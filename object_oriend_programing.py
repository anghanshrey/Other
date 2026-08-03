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



    











