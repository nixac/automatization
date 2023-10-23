#!/usr/bin/python
# Translates wine stacktraces to static adresses (so at 18h*Fh^7)
# @1: append to old value (default 0)
# @2: fallback source VA (default 0x0)
# @3: fallback target VA (default 0x180000000)
import sys

OLDADDRESS = sys.argv[1] == "1" if len(sys.argv) >= 2 else False
VABASE_DEFAULT = int(sys.argv[2].rstrip("h"), 16) if len(sys.argv) >= 3 else 0x0
VATARGET_DEFAULT = int(sys.argv[3].rstrip("h"), 16) if len(sys.argv) >= 4 else 0x180000000
VABASE = VABASE_DEFAULT
VATARGET = VATARGET_DEFAULT

print(f"Fallback source VA: {hex(VABASE)}", file=sys.stderr)
print(f"Fallback target VA: {hex(VATARGET)}", file=sys.stderr)
for line in sys.stdin:
    linebase = line
    try:
        if line.lower().strip().startswith("vabase:"):
            # Reconfigure VA for next lines
            valindex = line.lower().find("vabase:") + 7
            src, target, *_ = [x.strip() if len(x.strip()) else None for x in line[valindex:].strip().split("->") + [""]]
            if src == "SKIP":
                VABASE = 0
                VATARGET = 0
            else:
                VABASE = int(src.rstrip("h"), 16) if src else VABASE_DEFAULT
                VATARGET = int(target.rstrip("h"), 16) if target else VATARGET_DEFAULT

            line = f"{line[:valindex]} {hex(VABASE)} -> {hex(VATARGET)}"
        elif VABASE == 0 and VATARGET == 0:
            # Lines to be untouched
            raise
        else:
            # Lines to be translated
            srcaddrstr = line.strip()[:16]
            valindex = line.find(srcaddrstr)
            tgtaddr = VATARGET + int(srcaddrstr, 16) - VABASE
            tgtaddrstr=f"{hex(tgtaddr)} : {srcaddrstr}" if OLDADDRESS else f"{hex(tgtaddr)}"
            line = f"{line[:valindex]}{tgtaddrstr}{line[valindex+16:].rstrip()}"
        print(f"{line}")
    except:
        print(f"{linebase}", end="")
