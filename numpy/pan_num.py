class Student:

    def genrate_student(self):

        

    def display_student(self):
        pass


class Studentmangement:

    def __init__(self):
        self.students = Student()

    def student(self):
        while True:
            print(
                f"\n1. generate Student"
                f"\n2. display Student"
                f"\n3. Exit"
            )

            student_chocie = int(input("Enter your Choice : "))

            match student_chocie:
                case 1:
                    self.students.genrate_student()
                case 2:
                    self.students.display_student()
                case 3:
                    break

    def Mathematical(self):
        while True:
            print(
                f"\n1. Arithmatic operation"
                f"\n2. tegenomatriy"
                f"\n3. logerithm"
                f"\n4. main menu"
            )

            choice_mathe = int(input("Enter your Choice : "))

            match choice_mathe:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    break

        def random(self):
            pass

        def uuid(self):
            pass

    def run(self):
        print("\n-----------------------------------")
        print("          Student Data Analysis      ")
        print("-------------------------------------")
        while True:
            print(
                f"\n1. Student"
                f"\n2. Mathematical task"
                f"\n3. Random values"
                f"\n4. Uuid "
                f"\n5. Exit"
            )

            choice = int(input(("Enter Your Choice : ")))

            match choice:
                case 1:
                    self.student()
                case 2:
                    self.Mathematical()
                case 3:
                    self.random()
                case 4:
                    self.uuid()
                case 5:
                    print("thank you")
                    break
                case _:
                    print("Invaild choice plz vaild Number.")

system = Studentmangement()
system.run()

