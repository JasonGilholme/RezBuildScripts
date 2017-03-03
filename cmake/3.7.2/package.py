name = "googletest"

version = "1.8.0"

authors = [
    "Google"
]

description = \
    """
    Googles C++ testing framework
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "repository.googletest"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.GOOGLETEST_INCLUDE_DIR = "{root}/include"
