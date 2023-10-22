#!/usr/bin/env python3
# Transform array visually to display 16 elements per line
import sys
import pyperclip

if len(sys.argv) < 2:
    exit(1)
stin = pyperclip.paste() if sys.argv[1] == "clip" else sys.argv[1]

asarr = [x.strip() for x in stin.strip().split(",")]

output = ""
for i in range(0, len(asarr), 16):
    output += ", ".join(map(str, asarr[i : i + 16])) + ",\n"
output = output.rstrip("\n").rstrip(",")

if sys.argv[1] == "clip":
    stin = pyperclip.copy(output)
else:
    print(output)
