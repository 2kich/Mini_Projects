# Calculator
from art import logo


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        print("0 division")
        return
    return x / y


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    num1 = int(input("What's the first number?: "))
    for s in operations:
        print(s)

    continue_state = True
    while continue_state:
        op = input("Pick an operation from the list above: ")
        num2 = int(input("What's the second number?: "))
        func = operations[op]
        result = func(num1, num2)
        print(f"{num1} {op} {num2} = {result}")

        choice = input(
            f"Type 'y' if you would like to continue operations with {result}, or 'n' to start new calculation: "
        )
        if choice == "y":
            num1 = result
        else:
            continue_state = False
            calculator()


calculator()
