#!/usr/bin/env python3
# Translates internal documentation patch notations into js format expected by BemaniPatcher
import sys
import pyperclip

if len(sys.argv) < 2:
    exit(1)
stin = pyperclip.paste() if sys.argv[1] == "clip" else sys.argv[1]


[*rest, addr, on] = stin.split(":")
[off, on, *rest] = on.split("->")
off = ", ".join([f"0x{x}" for x in off.strip().split(" ")])
on = ", ".join([f"0x{x}" for x in on.strip().split(" ")])
addr = addr.strip()

output = f"{{ offset: {addr}, off: [{off}], on: [{on}] }},"
if sys.argv[1] == "clip":
    stin = pyperclip.copy(output)
else:
    print(output)
