def add_num():
    num_1 = input("First number: ")
    num_2 = input("Second number: ")
    try:
        total = int(num_1) + int(num_2)
    except ValueError:
        print("Please type only numbers.")
    else:
        print(f"Total: {total}")

add_num()