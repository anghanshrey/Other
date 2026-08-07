# E-commerce System

class Product:

    def __init__(self , product_id , name , price):

        self.product_id = product_id
        self.name = name
        self.__price = price

    # get method

    def get_price(self , getid):
        if self.product_id == getid:
            return self.__price
        else:
            print(f"invaild {getid}ID.")

    # set method

    def set_price(self , getid):
        if self.product_id == getid:
            new_price = float(input("Enter new price. : "))
            if new_price > 0:
                self.__price = new_price
                print("Price Updated Successfully!.")
            else:
                print("Invalid Price")
        else:
            print(f"invaild {getid}ID.")


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

    def buy(self, getid):
        if self.product_id == getid:
            print(f"{self.name}Order Placed Successfully!.")
            print("Thank You for Shopping with Us.")
        else:
            print(f"invaild id {getid}")

# main function

mobile1 = Mobile(101 , "iphone 17" , 90000 , "Apple" , 12 , 256 )
laptop1 = Mobile(102 , "DELL" , 105000 , "DELL" , 12 , 128 )
laptop2 = Mobile(103 , "mac book" , 200000 , "APPLE" , 8 , 256 )
mobile2 = Mobile(104 , "iphone 16" , 60000 , "Apple" , 8 , 64 )
mobile3 = Mobile(105 , "iphone 15" , 50000 , "Apple" , 8 , 128 )

while True:

    print("========== E-Commerce Menu =========")

    print("1. View Product")
    print("2. Check Price")
    print("3. Update Price")
    print("4. Buy Product")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        
        mobile1.display()
        laptop1.display()
        laptop2.display()
        mobile2.display()
        mobile3.display()

    elif choice == 2:

        
   

    elif choice == 3:

        get_id = int(input("Enter your id : "))

        mobile.set_price(get_id)

    elif choice == 4:

        get_id = int(input("Enter Buy id : "))
        mobile.buy(get_id)

    elif choice == 5:

        print("Thank You!!!!.")
        break

    else:

        print("Invalid Choice")
