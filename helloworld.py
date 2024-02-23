print("Hello World!")
/
choice = "sunny"
textcontent = ""

if choice == "sunny":
    textcontent = "It is nice and sunny outside today. Wear Short!Go to the beach, or the park, and get an ice cream."
elif choice ="rainy":
    textcontent = "Rain is falling outside; take a rain coat and an umbrella, and don't stay out for too long."
elif choice ="snowing":
    textcontent = "The snow is coming down - it is freezing! Best to stay in with a cup of hot chocolate, or go build a snowman."
elif choice = "overcase":
    textcontent = "It isn't raining, but the sky is grey and gloomy; it could turn  any minute, so take a rain coat just in case."
else:
    textcontent = ""

print(choice)
print(textcontent)

class Circle:
    pi=3.14159

    def __init(self,radius):
        self.radius = radius 

    def are(self):
        return self.pi * (self.radius **2)
    
    def circumstance():
        return 0 
    
class bankaccouny:
    def __init__(self,account_number,owner_name):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = 0
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw {amount}")
        else:
            print(f"Insufficient funds.")

    def display_balance(self):
        print(f"account_number:{self.account_number}")
        print(f"owner_name:{self.owner_name}")
        print(f"balance:{self.balance}")
