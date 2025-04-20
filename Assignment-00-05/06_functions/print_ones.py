def print_ones_digit(num):
  """Prints the ones digit of the given number."""
  print("The ones digit is", num % 10)

def main():
  """Prompts the user for a number and prints its ones digit."""
  num = int(input("Enter a number: "))
  print_ones_digit(num)

if __name__ == '__main__':
  main()
