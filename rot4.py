#!/usr/bin/python
import sys

if len(sys.argv) != 2:
    print("Usage: {} <input_string".format(sys.argv[0]))
    sys.exit(1)
input_string = sys.argv[1]
output = ""

for ch in input_string:
    output += chr(ord(ch) - 4)
print(output)
