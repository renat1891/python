try:
    num = int(input("Enter a number: "))
    print(5/num)
except ValueError:
    print("Invalid input. Please enter an integer.") 
except ZeroDivisionError:
    print("Division by zero is not allowed.")

