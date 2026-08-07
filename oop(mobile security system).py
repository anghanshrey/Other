class mobile_system:

    def __init__(self, name = str, password = str, status="locked"):

        self.name = name
        self.__password = password
        self.__status = status
        self.attempts = 1

    def unlock(self , Right_password):

        if self.__password == Right_password:
            self.__status = "unlocked"
            print("Mobile Security Started")
        else:
            if self.attempts == 3:
                print("Bye Bye (3 failed attempts!")
                return "exit"
            else:
                print(f"Attempt {self.attempts}/3 failed.")
                self.attempts += 1
                return False

    def lock(self):

        self.__status = "locked"
        print("Mobile locked Sucessfully.")

    def change_password(self ):

        if self.__status == "locked":
            print("First Unlocked phone")
            return
        else:
            self.__password = input("Enter New Password : ")
            print("change Password Sucessfully")

    def Display(self):

        print(f" ============== Modile Details ==============")
        print(f"\n Owner    :    {self.name} ")
        print(f"\n Status    :    {self.__status}")
        print(" ======================================")


name = input("Enter Your Name : ")
password = input("Enter Your password : ")

m1 = mobile_system(name , password)

while True:
    print("""
===== Menu =====
1. Unlock Moblie
2. lock Mobile
3. Change Password
4. Mobile Status
5. Exit
==============
""")

    choice = int(input(" Enter Choice:   "))

    match choice:
        case 1:
            while True:
                current_password = input("Enter Password : ")
                result = m1.unlock(current_password)

                if result == "exit":
                    exit()
                elif result == False:
                    continue
                else:
                    break
        case 2:
            m1.lock()
        case 3:
            m1.change_password()
        case 4:
            m1.Display()
        case 5:
            print("Thank you")
            break
        case _:
            print("Enter 1 to 5 Number Only!")
