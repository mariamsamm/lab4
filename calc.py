
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation!"


# Example
print(calculator(10, 5, "+"))  # 15
print(calculator(10, 5, "-"))  # 5
print(calculator(10, 5, "*"))  # 50
print(calculator(10, 5, "/"))  # 2.0
