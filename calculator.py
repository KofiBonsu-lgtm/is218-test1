""" Simple calculator functions """

def add (a,b):
    """Adds two numbers"""
    return a+b

def subtract (a,b):
    """Subtracts second number from first"""
    return a-b

def multiply (a,b):
    """Multiplies two numbers"""
    return a*b

def divide (a,b):
    """Divides first number by second"""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a/b
