import uuid
import time
from datetime import datetime
import random
import math
import numpy as np

class Studentmanagement:

    def __init__(self):

        self.name = "Shrey Anghan"
        self.student_id = str(uuid.uuid4())
        self.marks = [random.randint(35, 95) for i in range(10)]

    def student_details(self):
        print("=======================================")
        print("   STUDENT DATA ANALYSIS PROGRAM       ")
        print("=======================================")

        print("Student Name : ",self.name)
        print("Student ID   : ",self.student_id)
        print("Current Date : ",datetime.now().date())
        print("Current Time : ",time.strftime("%I:%M:%S %p"))

        print()

    def display_marks(self):

        print("Original Marks :\n",self.marks)
        print()

    def higher_order_function(self):

        print("Sorted Marks :\n",sorted(self.marks))
        print("Squared_marks :\n",
              list(map(lambda x : x ** 2, self.marks)))
        print("Marks Greater Than 50 :\n",
        list(filter(lambda x : x > 50, self.marks))
        )

    def mathematical_calculation(self):

        total = sum(self.marks)
        average = total/ len(self.marks)

        square_root = math.sqrt(total)
        power_value = math.pow(average, 2)

        print("Mathematical Calculations:")
        print("Total Marks         :", total)
        print("Average Marks       :", round(average, 2))
        print("square Root Total   :", round(square_root, 2))
        print("Average Squared     :", round(power_value, 2))

    def create_numpy_array(self):

        self.marks_array = np.array(self.marks)

        print("Numpy Array :\n",self.marks_array)

    def array_creation(self):

        print("Numpy Array Creation:")

        print("Zeros Array :\n",np.zeros(5, dtype=int))
        print("Ones Array :\n",np.ones(5, dtype=int))
        print("Range Array :\n", np.arange(1, 6))

        print()

    def array_index(self):

        print("Numpy Indexing :")

        print("First Mark :",self.marks[0])
        print("Third Mark :",self.marks[2])
        print("Last Mark :",self.marks[-1])

        print()


    def main(self):

        self.student_details()
        self.display_marks()
        self.higher_order_function()
        self.mathematical_calculation()
        self.create_numpy_array()
        self.array_creation()
        self.array_index()

if __name__=="__main__":

    system = Studentmanagement()

    system.main()

