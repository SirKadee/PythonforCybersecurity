#!/usr/bin/env python3
# Sample script that writes to a file
# By Devin Van

# open file for writing
f = open("testfile.txt", "w")

# Write some content to file
print("Hello World")
f.write("Hello World\n")
f.write("Hello World\n")
f.write("Hello World\n")

# Close the file
f.close()