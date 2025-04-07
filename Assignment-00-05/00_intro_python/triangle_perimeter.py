def main():
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))
    Formula : str = str(side1 + side2 + side3)
    print(f"The perimeter of the triangle is : {Formula}")

if __name__ == '__main__':
    main()