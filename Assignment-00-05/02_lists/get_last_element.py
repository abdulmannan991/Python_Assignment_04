def get_last_element(lst):
    print(lst[len(lst) - 1])

    
def get_last():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
     lst = get_last()
     get_last_element(lst)



if __name__ == '__main__':
    main()

