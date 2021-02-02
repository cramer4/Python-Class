###########################################################
with open("learning_python.txt") as file:
    contents = file.read()
    print(contents.strip())
###########################################################
file = "learning_python.txt"
with open("learning_python.txt") as file:
    for line in file:
        print(line.rstrip())
print("")
###########################################################
with open("learning_python.txt") as f:
    for l in f:
        lines = f.readlines()

    for line in lines:
        print(line.rstrip())
###########################################################