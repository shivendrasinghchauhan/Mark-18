while True:
    print("Press 1 for addition \nPress 2 for subtraction \nPress 3 for multiplication \nPress 4 to exit")
    n = int(input("Enter your choice: "))
    
    if n == 1:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        z = x + y
        print(f"Addition of {x} and {y} is {z}")
        
    elif n == 2:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        z = x - y
        print(f"Subtraction of {x} and {y} is {z}")
        
    elif n == 3:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        z = x * y
        print(f"Multiplication of {x} and {y} is {z}")
        
    elif n == 4:
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
