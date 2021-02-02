def add_num_loop():
    print('This is addition calculator. Type two numbers to add together.\nType"q" to quit.\n')
    while True:

        num_1 = input("First number: ")
        if num_1 == "q":
            break
        else:
            num_2 = input("Second number: ")
        if num_2 == "q":
            break
        else:
            try:
                total = int(num_1) + int(num_2)
            except ValueError:
                print("Please type only numbers.")
            else:
                print(f"Total: {total}")

add_num_loop()