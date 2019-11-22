# Matt Landale
# Lab 9

class BankAccount:

    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def pincheck(self, pin):
        pin = input("Enter Pin: ")
        if pin == self.pin:
            return True
        else:
            print("Error try again")
            
    
    def deposit(self, amount):
        self.balance += amount
        return self
        
        
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient Funds! Balance is only {self.balance}. Your widthdrawal request of {amount} can't be completed.")
        else:
            self.balance = self.balance - amount
        return self
    
    def get_balance(self, amount):
        return self.balance

b1 = BankAccount('0509')
d1 = 0

print('Matt Landale: ')
y1 = int(input("Enter 1 to make withdrawl. Enter 2 to make a deposit."))
if y1 == 1:
    w1 = int(input("How much do you want to withdraw: "))
    print("Withdrawl: $")
else:
    d1 = int(input("How much do you want to deposit: "))
    b1.deposit(d1)
    print("Current Balance: $", amount)

          
                      

        
        


        
