def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b


while True:
    print("\n====== ADVANCED CALCULATOR ======")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Modulus (%)")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "7":
        print("Calculator Closed. Thank you 🙏")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))

    elif choice == "2":
        print("Result:", subtract(num1, num2))

    elif choice == "3":
        print("Result:", multiply(num1, num2))

    elif choice == "4":
        print("Result:", divide(num1, num2))

    elif choice == "5":
        print("Result:", power(num1, num2))

    elif choice == "6":
        print("Result:", modulus(num1, num2))

    else:
        print("Invalid choice ❌ Try again")
