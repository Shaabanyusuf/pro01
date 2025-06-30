def calculator(a, b, operation):

    if operation == "a":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mult":
        return a * b
    elif operation == "div":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
