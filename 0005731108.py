""" Game fix for IIDX (UID:0005731108)
"""
# Protonfix for games supporting Windows 8 prefix
# This protonfix expects prefix shared between multiple titles
# Explicitely set overrides for all dlls fetched here even when not using them
# pylint: disable=C0103

import os
from protonfixes import util


def main():
    # Generic environment (may be overwritten by subpatch)
    util.protontricks("win8")
    util.protontricks("sound=alsa")

    # Apply optional patches (without bloating protonfixes)
    patches = (os.getenv("PROTON_STYLE_PATCH") or "").strip(":")
    try:
        for patch in patches.split(":") if len(patches) else []:
            globals()[f"iidx_{patch}"]()
    except KeyError as err:
        print(f"gamefix: no patch available for {err}")

def iidx_30():
    # explicit to keep constant behaviour with other games (iidx27)
    util.set_environment("WINEDLLOVERRIDES", "d3dcompiler_43,d3dx9_43=b,n")


def iidx_29():
    # explicit to keep constant behaviour with other games (iidx27)
    util.set_environment("WINEDLLOVERRIDES", "d3dcompiler_43,d3dx9_43=b,n")

def iidx_28():
    # explicit to keep constant behaviour with other games (iidx27)
    util.set_environment("WINEDLLOVERRIDES", "d3dcompiler_43,d3dx9_43=b,n")


def iidx_27():
    # crash at 0x180176996, shader compilation fails for D3DXAssembleShader() - crash with missing callback Direct3DShaderValidatorCreate()
    util.protontricks("d3dcompiler_43")
    util.protontricks("d3dx9_43")
    # this exact override needed for subscreen to be created
    util.set_environment("WINEDLLOVERRIDES", "d3dcompiler_43=n,b")

def iidx_26():
    # explicit to keep constant behaviour with other games (iidx27)
    util.set_environment("WINEDLLOVERRIDES", "d3dcompiler_43,d3dx9_43=b,n")

def iidx_25():
    # explicit to keep constant behaviour with other games (iidx27)
    util.set_environment("WINEDLLOVERRIDES", "d3dcompiler_43,d3dx9_43=b,n")

def tests():
    # Most dlls that may or may not be required
    util.set_environment("WINEDLLOVERRIDES", "quartz,devenum,dmime,dmsynth,dmloader,dmusic,dsound,dsdmo,msdmo,bmsound-wine,d3dx9_41,d3dx9d_41,d3dx9_43,d3dcompiler_43=n,b")
    pass
