# Perform calculation
def calculation(num1,num2,choice):
    if choice == "1":
        result = num1 + num2
        print("Result =", result)

    elif choice == "2":
        result = num1 - num2
        print("Result =", result)

    elif choice == "3":
        result = num1 * num2
        print("Result =", result)

    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print("Result =", result)
        else:
            print("Error: Division by zero is not allowed.")

    else:
        print("Invalid choice. Please select a valid operation.")