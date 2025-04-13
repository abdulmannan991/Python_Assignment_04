def main():
    lst = []
    user = input("Enter a value: ")
    while user != "":
        lst.append(user)
        user = input("Enter a value: ")


    print(f"Here is the list : {lst}")



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()