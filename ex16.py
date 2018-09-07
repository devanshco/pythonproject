# Argument Variable
from sys import argv

# Asking the user to input Script (ie. .py file name) Name and filename (ie. text/.txt file name)
script, filename = argv

# Print Commands
print(f"We're going to erase {filename},")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Asking user input
input("?")

# 'w' here means to open file in write mode
print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Gooddbye!")

# Truncate here means to clean/format the file
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
# "\n" means to move to the next line
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")

# target.close()
