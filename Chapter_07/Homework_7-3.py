number = input("Please type a number: ")
number = int(number)
number = number % 10

if number == 0:
    print("The number you have typed is a multiple of ten.")
else:
    print("The number you have typed is not a multiple of ten.")