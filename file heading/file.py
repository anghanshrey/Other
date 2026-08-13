# Python File Handing

# text file handling

# open() function

# file = open('filename.txt' , 'mode')

'''
Mode               Meaning
r                         Read
w                        Write
a                         Append
x                        create new file
r+                        Read + Write
w+                      Write + Read
a+                      Append + Read
r-                         Read
'''

"""
files = open("demo.txt" , "w")

files.write("vivek\n")
files.write("Python\n")
files.write("Red and White\n")

files = open("demo.txt" , "r")

data = files.read()

print(data)

files.close()

file = open("demo.txt" , "a")

file.write("Javascript")

file = open("demo.txt" , "r")

data = file.read()

print(data)

file.close()

file = open("demo.txt" , "r")

#print(file.readline())
#print(file.readline())

print(file.readlines())
"""
"""
file = open("student.txt" , "x")

file.close()
"""

"""
file = open("student.txt" , "w")

file.write("My name is  Shrey.")
file.write("I am 21 years old.")

file = open("student.txt" , "r")

print(file.readlines())

file.close()
"""
