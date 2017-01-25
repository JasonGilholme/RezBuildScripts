name = "avrlibc"

version = "2.0.0"

authors = [
    "GNU"
]

description = \
    """
    Standard AVR Libs
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-14.04"]
]

uuid = "repository.avrlibc"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/avr/lib")
    env.AVRLIBC_INCLUDE_DIR = "{root}/avr/include"
