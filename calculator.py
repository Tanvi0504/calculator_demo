# This is the caluculator demo to learn git hub workflow



def add(a,b):
    return a+b

def sub(a,b):
    return a-b

number1 = int(input("Enter First number: "))
number2 = int(input("Enter second number: "))
operator = input("Enter +,-,*,/: ")
if (operator == "+"):
    print (add(number1,number2))
elif (operator == "-"):
    print(sub(number1,number2))
elif (operator == "*"):
    print()
elif (operator == "/"):
    print()
else:
    print("Unknown Operator")
    
