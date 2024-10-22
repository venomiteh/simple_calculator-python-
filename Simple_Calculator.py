def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_action_input():
    valid_actions = ['+', '-', '*', '/', 'clear', 'done']
    while True:
        action = input("Choose an operation (+, -, *, /) or 'clear' to reset or 'done' to stop: ").lower()
        if action in valid_actions:
            return action
        else:
            print("Invalid operation. Please enter one of the following: +, -, *, /, clear, done.")

def calculator():
    result = 0
    first_operation = True
    go = True

    while go:
        print(f"Result: {result}")
        action = get_action_input()
        if action == 'clear':
            result = 0
            print("Calculator reset!")
            continue  
        elif action == 'done':
            print(f"Final result: {result}")
            go = False  
            continue

        if first_operation:
            num1 = get_float_input("Enter Number 1: ")
            first_operation = False  
        else:
            num1 = result  

        num2 = get_float_input("Enter Number 2: ")  

        if action == '+':
            result = addition(num1, num2)
        elif action == '-':
            result = subtraction(num1, num2)
        elif action == '*':
            result = multiplication(num1, num2)
        elif action == '/':
            division_result = division(num1, num2)
            if isinstance(division_result, str):  
                print(division_result)
            else:
                result = division_result
        else:
            print("Invalid operation. Please try again.")

calculator()