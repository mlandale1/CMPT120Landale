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
