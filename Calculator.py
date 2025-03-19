def addition(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        return "Error: Please provide numeric inputs."

# Example usage
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print(safe_addition(num1, num2))
