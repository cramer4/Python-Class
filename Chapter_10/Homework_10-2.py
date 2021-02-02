with open("learning_python.txt") as file:
    contents = file.read()
    contents = contents.replace('Python', 'C')
    print(contents.strip())