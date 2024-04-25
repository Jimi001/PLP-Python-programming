# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1\n")
        file.write("12345\n")
        file.write("Line 3 with some more text\n")
except IOError:
    print("An error occurred while creating the file.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to read the file.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is an appended line\n")
        file.write("67890\n")
        file.write("Another appended line\n")
except IOError:
    print("An error occurred while appending to the file.")


