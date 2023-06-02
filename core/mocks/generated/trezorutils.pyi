from typing import *


# extmod/moddetahardutils/moddetahardutils-meminfo.h
def meminfo(filename: str) -> None:
    """Dumps map of micropython GC arena to a file.
    The JSON file can be decoded by analyze.py
    Only available in the emulator.
     """


# extmod/moddetahardutils/moddetahardutils.c
def consteq(sec: bytes, pub: bytes) -> bool:
    """
    Compares the private information in `sec` with public, user-provided
    information in `pub`.  Runs in constant time, corresponding to a length
    of `pub`.  Can access memory behind valid length of `sec`, caller is
    expected to avoid any invalid memory access.
    """


# extmod/moddetahardutils/moddetahardutils.c
def memcpy(
    dst: bytearray | memoryview,
    dst_ofs: int,
    src: bytes,
    src_ofs: int,
    n: int | None = None,
) -> int:
    """
    Copies at most `n` bytes from `src` at offset `src_ofs` to
    `dst` at offset `dst_ofs`. Returns the number of actually
    copied bytes. If `n` is not specified, tries to copy
    as much as possible.
    """


# extmod/moddetahardutils/moddetahardutils.c
def halt(msg: str | None = None) -> None:
    """
    Halts execution.
    """


# extmod/moddetahardutils/moddetahardutils.c
def firmware_hash(
    challenge: bytes | None = None,
    callback: Callable[[int, int], None] | None = None,
) -> bytes:
    """
    Computes the Blake2s hash of the firmware with an optional challenge as
    the key.
    """


# extmod/moddetahardutils/moddetahardutils.c
def firmware_vendor() -> str:
    """
    Returns the firmware vendor string from the vendor header.
    """


# extmod/moddetahardutils/moddetahardutils.c
def reboot_to_bootloader() -> None:
    """
    Reboots to bootloader.
    """
SCM_REVISION: bytes
VERSION_MAJOR: int
VERSION_MINOR: int
VERSION_PATCH: int
USE_SD_CARD: bool
MODEL: str
EMULATOR: bool
BITCOIN_ONLY: bool