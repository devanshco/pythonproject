# Importing Argument Variable Module
from sys import argv

# Getting Values for Argument Variable
script, filename = argv

# Variable To Look for the file
txt = open(filename)

""" Print Commands to print the filename and Variable Content ie the file Content
print(f"Here's your file {filename}:")
print(txt.read())

# Print Command and Variable to get user input
print("Type the filename again:")
file_again = input(">> ")

txt_again = open(file_again)

print(txt_again.read())
"""
