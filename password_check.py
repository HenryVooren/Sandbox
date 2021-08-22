"""
CP1404/CP5632 - Practical
Password checker
"""

MIN_LENGTH = 9

password = input("Enter Password > ")
while len(password) < MIN_LENGTH:
    print("Invalid password entered")
    password = input("Enter Password > ")

for i in range(0, len(password)):
    print("*", end="")
