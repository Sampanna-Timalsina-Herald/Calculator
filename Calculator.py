#Calculator App
def divide(num1,num2):
    if (num2 == 0):
        print("Cannot Divide By 0")
        return 0
    print(f"{num1} divided by {num2} is:{num1/num2:.2f}")
def user_input():
    validInput = True
    while(validInput):
        try:
            number1 = int(input("Enter number 1:"))
            number2 = int(input("Enter number 2:"))
            print("1.Add\n2.Subtract\n3.Divide\n4.Multiply\n")
            choice = int(input("Enter choice:"))
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                divide(number1,number2)
            elif choice == 4:
                pass
            else:
                print("Enter a valid choice")
            validInput = False
        except ValueError:
            print("Error:Enter a valid number")
       
user_input()

