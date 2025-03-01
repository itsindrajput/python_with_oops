class Atm:
  def __init__(self): 
    self.pin = None
    self.balance = 0
    self.menu()

  def menu(self):
    while True:
      userInput = input("""
    Welcome to Mu Atm!
    1. Enter 1 to Create Pin
    2. Enter 2 to Withdraw Cash
    3. Enter 3 to Deposit Cash
    4. Enter 4 to Check Balance
    5. Enter 5 to exit
    Enter your choice: 
    """)
  
      if(userInput == "1"):
        # print("You Can Create Pin Here")
        self.create_pin()
        
      elif(userInput == "2"):
        # print("Withdraw Cash Here") 
        self.withdraw()
        
      elif(userInput == "3"):
        # print("Deposit Cash Here") 
        self.deposit()
        
      elif(userInput == "4"):
        # print("Check You Account Balance")   
        self.check_balance()
        
      elif (userInput == "5"):
        print("Exiting...")
        break
      else:
        print("Invalid choice. Please try again.")
    
  def create_pin(self):  
    self.pin = input("Enter Your Pin: ")
    print("Pin Created Successfully!")
      
  def deposit(self):
    tpin = input("Enter Your Pin: ")
    if(tpin == self.pin):
      amount = int(input("Enter The Deposit Amount: "))
      self.balance += amount
      print(f"Deposit Successful! New Balance: {self.balance}")
    else: 
      print("Incorrect PIN!")
      
  def withdraw(self):
    tpin = input("Enter Your Pin: ")
    if(tpin == self.pin):
      amount = int(input("Enter withdrawal amount: "))
      if(amount < self.balance):
        self.balance -= amount
        # self.balance = self.balance - amount
        print(f"Withdrawal successful! Remaining Balance: {self.balance}")
      else:
        print("Insufficient balance.")
    else:
      print("Incorrect PIN!")

  def check_balance(self):
    tpin = input("Enter Your Pin: ")
    if(tpin == self.pin):
      print(f"Your balance is: {self.balance}")  
    else:
      print("Incorrect PIN!") 
      
user1 = Atm()