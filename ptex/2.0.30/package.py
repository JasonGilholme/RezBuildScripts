name = "ptex"

version = "2.0.30"

authors = [
    "Disney"
]

description = \
    """
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "repository.ptex"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PTEX_INCLUDE_DIR = "{root}/include"
