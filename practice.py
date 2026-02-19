try:
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        content = file.read()
        print(content)
        words = content.split()
        print("Number of words:", len(words))

except FileNotFoundError:
    print("File not found. Please check the file name.")

except PermissionError:
    print("You do not have permission to access this file.")

finally:
    print("Program ended.")
