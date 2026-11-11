class BankAccount:
    def __init__ (self,acname,acnumber,password,balance):
        self.acname=acname
        self.__acnumber=acnumber
        self.__password=password
        self.__balance=balance   
    def display(self):
        print(f"hiii {self.acname}")
    def deposit(self,amount):
        
        if amount>0:
            # self.balanace+=amount
            self.__balance=self.__balance+amount
            print(f"amount deposited {self.__balance}")
        else:
            print("deposited amount must be positive")
            
            
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
              self.__balance-=amount
              print(f"amount deducted {self.__balance}")
        else:
         print("insufficinet balamnce") 
    def get_balance(self):
        print(self.__balance)
        
b=BankAccount("sai tharun ","asdf1123","as@123",2000)
b.display()