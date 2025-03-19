#Calculator App
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "error: Division by zero is not allowed"
    