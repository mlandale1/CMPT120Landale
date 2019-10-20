# JA: Maybe you misunderstood the project, but you are supposed to be
# able to solve a complete equation, not just a simple one operator equation

# You need to get this working for the second project. Stop by my office if
# you need help.

def add(a, b):
   return a + b

 
def subtract(a, b):
   return a - b


def multiply(a, b):
   return a * b


def divide(a, b):
   return a / b

print("Select operation.")
print("+.Add")
print("-.Subtract")
print("*.Multiply")
print("/.Divide")


choice = input("Enter choice(+ / - / * / / ):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '+':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '-':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '*':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '/':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
