def add(a,b):
  return a + b

def subtract(a,b):
  return a - b

def multiply(a,b):
  return a * b

def divide(a,b):
  if b == 0:
    return("cannot be divided by zero")
  else:
    return a / b

def modulus(a,b):
  return a % b

def power(a,b):
  return a ** b

def calculator():
  print("SIMPLE PYTHON CALCULATOR")
  

  while True:
    print("""OPERATIONS
    1.ADDITION
    2.SUBTRACTION
    3.MULTIPLICATION
    4.DIVISION
    5.MODULUS
    6.POWER
    7.EXIT
    """)

  try:
    choice = int(input("Enter your choice: "))
    if choice == 7:
      print("THANKYOU FOR USING THE CALCULATOR!")
    if choice < 1 and choice > 7:
      print("INVALID CHOICE!")
      continue

    num1 = int(input("Enter your first number: "))

    num2 = int(input("Enter your second number: ))
                     
    if choice == 1:
      print("Add num1,num2: ")
    elif choice == 2:
      print("Subtract num1,num2: ")
    elif choice == 3:
      print("Multiply num1,num2: ")
      
                 

