"""
Project #1: Basic Calculator with User Input
Category: Python Programming

Build a command-line calculator that takes two numbers and an operation (add, subtract, multiply, divide) from the user and returns the result. This introduces basic Python syntax, user input handling, and conditional statements. For example, if the user inputs '5', '3', and '+', the program outputs '8'. You'll learn about variables, data types (int, float), and control flow (if-else). Error handling for invalid inputs (e.g., division by zero) is introduced.
"""

# Start your implementation here...


while True:
    try:

        num1 =float(input("Entre first number:")) 
        num2 =float(input("Entre second number:"))
        break
    except Exception as e:
        print('Entre a valid rational number: ')
    
        
     

print(f"Sum of {num1} and {num2} is ",num1 + num2)
print(f"Difference of {num1} and {num2} is ",num1 - num2)

print(f"Product of {num1} and {num2} is ",num1 * num2)
if num2 != 0:
    print(f"{num1} by {num2} is ",num1 / num2)
else:
    print("Can not divide  by Zero is not possible. ")






