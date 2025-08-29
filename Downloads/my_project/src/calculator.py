def sum(a,b):
    return a + b

def minus(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    print("Sum:", sum(10, 5))
    print("Minus:", minus(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))
    print("Divide by zero:", divide(10, 0))
