#!/usr/bin/env python3
# A simple "Hello World" script in python
# Created 4/13 by Devin

# ask user for their name
user_name = input("What is your name: ")

# Write Hello using concatenation
print("Hello " + user_name)

# string formatting and f-string
print("Hello {0}".format(user_name))
print(f"Hello {user_name}")

# multiple print statements
print("Hello", user_name)
print("Hello ", end="")
print(user_name)

# Create new variables
message = "Hello " + user_name
print(message)

# join text
print( " ".join(["Hello", user_name]))

# old style formatting
print("Hello %s" % user_name)