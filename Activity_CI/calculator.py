def add(num1, num2): 
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
         return "Error"
    return num1 + num2

def subtract(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
         return "Error"
    return num1 - num2