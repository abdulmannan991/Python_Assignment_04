def main():
    degree_Fahrenheit : str = input("Enter temperature in Fahrenheit: ")
    degree_Fahrenheit : float = float(degree_Fahrenheit)
    degree_celsius : float = (degree_Fahrenheit-32) * 5.0/9.0
    print(f"Temperature: {degree_celsius:.2f}°C")



if __name__ == '__main__':
    main()