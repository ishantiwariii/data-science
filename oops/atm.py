class Atm:
  #we are using constructor
  def __init__(self):
    self.__pin = '' 
    self.__balance = 0
    self.menu()
    print("thanks for visiting us ")

  def menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)

    if user_input == "1":
      self.create_pin()
    elif user_input=="2":
      self.change_pin()
    elif user_input=="3":
      self.check_bal()
    elif user_input=="4":
      self.withdraw()
    else:
      pass

  def create_pin(self):
    print("hey there wassup!")
    user_pin=int(input("enter your pin: "))
    self.__pin = user_pin

    user_bal = int(input("enter your balance: "))
    self.__balance = user_bal
    self.menu()

  def change_pin(self):
    pin = int(input("enter your old pin: "))
    if pin == self.__pin:
      new_pin=int(input("enter your new pin: "))
      self.__pin=new_pin
      print("pin successfully changed")
    else:
      print("you have entered the wrong pin")
    self.menu()

  def check_bal(self):
    user_pin=int(input("enter your pin "))
    if user_pin==self.__pin:
      print(f"here is your current balance {self.__balance}")
    
    else:
      print("you have entered the wrong pin")
    self.menu()

  def withdraw(self):
    user_pin=int(input("enter your pin "))
    if user_pin == self.__pin:
      withdraw_bal = int(input("enter the balance for withdrawal: "))
      if withdraw_bal<=self.__balance:
        self.__balance-=withdraw_bal
        print("transaction successful")
        print(f"your new current balance is {self.__balance}")
      else:
        print("your bank balance is less than the entered withdrawel balance")
    else:
      print("you have entered wrong pin ")
    self.menu()


user_1 = Atm()
