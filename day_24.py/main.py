# file = open("file/path.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("file/path.txt") as file:
    contents = file.read()
    print(contents)

with open("file/path.txt", mode="w") as file:
    file.write("New text.")

with open("file/path.txt", mode="a") as file:
    file.write("\nNew text.")

with open("file/path.txt", mode="a") as file:
    file.write("New text.")



