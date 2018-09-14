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
ok = open(filename, 'w')

print("Truncating the file. Gooddbye!")

# Truncate here means to clean/format the file
ok.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

ok.write(line1)
# "\n" means to move to the next line
ok.write("\n")
ok.write(line2)
ok.write("\n")
ok.write(line3)
ok.write("\n")

print("And finally, we close it.")


# Don't know why we used this close command
ok.close()
