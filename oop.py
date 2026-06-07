# from decimal import Decimal


# class Account:

#     def __init__(self, name, balance):
#         self.balance = Decimal(balance)
#         if self.balance < Decimal("0.00"):
#             raise ValueError("Initial balance must be >= to 0.00")
#         self.name = name

#     def deposit(self, amount):
#         amount_decimal = Decimal(amount)
#         if amount_decimal < Decimal("0.00"):
#             raise ValueError("Deposit amount must be positive")
#         self.balance += amount_decimal

#     def withdraw(self, amount):
#         amount_decimal = Decimal(amount)
#         if amount_decimal > self.balance:
#             raise ValueError("Insufficient funds")
#         elif amount_decimal < Decimal("0.00"):
#             raise ValueError("Withdraw amount must be positive")
#         self.balance -= amount_decimal


# user_name = input("Enter account holder name: ")
# user_balance = input("Enter initial balance: ")

# account1 = Account(user_name, user_balance)

# dep_amount = input("Enter amount to deposit: ")
# account1.deposit(dep_amount)

# with_amount = input("Enter amount to withdraw: ")
# account1.withdraw(with_amount)


# print(f"Account Holder: {account1.name}")
# print(f"Final Balance: ${account1.balance}")
'''
encapsulation
'''
# class Time:
#     def __init__(self, hour=0, minute=0, second=0):
#         self.hour = hour
#         self.minute = minute
#         self.second = second

#     @property
#     def hour(self):
#         return self._hour

#     @hour.setter
#     def hour(self, hour):
#         if not (0 <= hour < 24):
#             raise ValueError(f'hour ({hour}) must be 0-23')
#         self._hour = hour

#     @property
#     def minute(self):
#         return self._minute

#     @minute.setter
#     def minute(self, minute):
#         if not (0 <= minute < 60):
#             raise ValueError(f'minute ({minute}) must be 0-59')
#         self._minute = minute

    
#     @property
#     def second(self):
#         return self._second

#     @second.setter
#     def second(self, second):
#         if not (0 <= second < 60):
#             raise ValueError(f'second ({second}) must be 0-59')
#         self._second = second



# wake_up = Time(hour=6, minute=30, second=12)
# print(wake_up.hour)
# wake_up.hour = 7
# print(wake_up.hour)

# print(wake_up.minute)
# wake_up.minute = 45
# print(wake_up.minute)

# print(wake_up.second)
# wake_up.second = 50
# print(wake_up.second)

# class ScoreBoard:
#     def __init__(self, score):
#         self.__score = score

#     def get_score(self):
#         return self.__score


# s1 = ScoreBoard(0)
# print(s1.get_score())
'''
inner class
'''

# class outer:
#     def __init__(self):
#         self.name="outer class"
# class inner:
#  def __init__(self):
#   self.name="inner class"
# def display(self):
#  print("This is an inner class")
# outer=outer()
# print(outer.name)
                    
'''
inner class from outside
'''
# class outer:
#     def _init(self):
#         self.name=("outer")
# class inner:
#     def __init(self):
#        self.name=("inner")
#        def display(self):
#            print("hi from inner class")
# outer=outer()
# inner=outer.inner()
# inner.display()
'''
outer from inner class
'''
# class outer:
#     def __init__(self):
#         self.name=("samrat")
# class inner:
#     def __init__(self,outer):
#         self.outer=outer
#     def display(self):
#         print(f"outer class name:{self.outer.name}")
# outer=outer()
# inner=outer.inner(outer)
# inner.display()

'''
# car engine
# '''
# class engine:
#     def __init__(self):
#         self.status = "off"

#     def start(self):
#         self.status = "Running"
#         print("Engine Started")  

#     def stop(self):
#         self.status = "off"
#         print("Engine stopped")  


# class car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self.engine = engine()  


#     def drive(self):
#         if self.engine.status == "Running":
#             print(f"Driving the {self.brand} {self.model}")
#         else:
#             print("Start the engine first")





# my_car = car("Toyota", "Corolla")


# my_car.drive()


# my_car.engine.start()


# my_car.drive()

''''
inheritance
'''   
class person:
    def __init__(self,fname,lname):
     self.firstname=fname
     self.lastname=lname
     def printname(self):
      print(self.firstname,self.lastname)
x=person("Samundra","kunwar")
x.printname()
'''
super()it inherit class method and properties'''

  
  
    
                  

        
        
