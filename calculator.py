# Basic Calculator App

# Variables with Inputs
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Addition Operator
if operator == "+":
    result = num1 + num2
# Subtraction Operator
elif operator == "-":
    result = num1 - num2
# Multiplication Operator
elif operator == "*":
    result = num1 * num2
# Division Operator
elif operator == "/":
    # Check for division by 0
    if num2 == 0:
        print("Error: Division by 0")
    else:
        result = num1 / num2
# Check for non operators 
else:
    result = "Invalid operator"

print("Result:", result)