#!/usr/bin/env python3
# example workign with Functions
#By Devin Van

#Create The Function
def print_me(message):
  print(message)
  return("returned value")

#Call The Function
print("Before Function")

error_message = "This is an error"
returned_value = print_me(error_message)
print(returned_value)

print("After Function")