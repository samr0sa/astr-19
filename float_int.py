def python_math(define):
    while True:
        try:
            print()
            int_num1 = int(input("Enter an integer: "))
            break  
            # Breaks  loop of asking user to input
            # correct value if the input is a valid integer
        except ValueError:
            print("Not quite right. Please enter an integer.")

    # Input from the user for the second integer
    while True:
        try:
            print()
            int_num2 = int(input("Enter another integer: "))
            break
        except ValueError:
            print("Not quite right. Please enter an integer.")

    # Input from the user for the first floating-point number
    while True:
        try:
            print()
            float_num1 = float(input("Enter a floating point number: "))
            break  
        except ValueError:
            print("Not quite right. Please enter a floating-point number.")

    # Input from the user for the second float
    while True:
        try:
            print()
            float_num2 = float(input("Enter another floating point number: "))
            break  
        except ValueError:
            print("Not quite right. Please enter a floating-point number.")

    # Perform the operations
    sum_ = float_num1 + float_num2
    difference_ = int_num1 - int_num2
    product_ = float_num1 * int_num1

    # Print the results and their data types
    print()
    print(f"Sum: {float_num1} + {float_num2} = {sum_}\nData Type: {type(sum_)}")
    print()
    print(f"Difference: {int_num1} - {int_num2} = {difference_}\nData Type: {type(difference_)}")
    print()
    print(f"Product: {float_num1} * {int_num1} = {product_}\nData Type: {type(product_)}")
    print()


if __name__ == "__main__":
    print()
    print(f"\033[4mFloat vs Integer Numbers\033[0m")
    print()
    
    while True:
        define = input("Enter integers and floats when prompted. Hit the 'enter' key to continue. Type 'exit' when done with program: ")
        
        # However, if user is done, exit command to exit code
        if define.lower() == 'exit':
            print()
            print(f"Until text time.")
            print()
            break  # Exit the loop if the user enters 'exit'
       
        # Will contiune to run program
        # until user inputs 'exit'
        python_math(define)
