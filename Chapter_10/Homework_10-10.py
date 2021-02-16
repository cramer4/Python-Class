def word_count(book_name):
    try:
        file = book_name
        with open(file) as file_object:
            book = file_object.read()
            thes = book.lower().count("the")
            the_s = book.lower().count("the ")
            print(thes)
            print(the_s)
    except FileNotFoundError:
        print("File or directory not found")
    else:
        book.lower().count("the")

word_count('sherlock_holmes.txt')