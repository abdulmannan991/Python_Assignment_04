def main():
    print("This program adds two numbers.")
    num1 : str = input("Enter first number: ")
    num1 : int = int(num1)
    num2 : str = input("Enter second number: ")
    num2 : int = int(num2)
    result : int = num1 + num2
    print("The sum of 2 numbers is :" + str(result) + ".")

    
if __name__ == '__main__':
    main()