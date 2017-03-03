name = "double_conversion"

version = "1.1.5"

authors = [
    "Google"
]

description = \
    """
    Efficient binary-decimal and decimal-binary conversion routines for IEEE doubles.
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "repository.double_conversion"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.DOUBLE_CONVERSION_INCLUDE_DIR = "{root}/include"
