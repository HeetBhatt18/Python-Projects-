
num1 = float(input("Enter The first number:"))
num2 = float(input("Enter The second number:"))

print("Chose opertaion:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Divison (/)")

choice = (input("Enter your choice (1/2/3/4): "))

if choice == "1":
    print("Result:", num1 + num2)

elif choice == "2":
    print("Result:", num1 - num2)

elif choice == "3":
    print("Result:", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")

else:
    print("Invalid choice")