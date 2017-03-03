name = "qt"

version = "5.8.0"

authors = [
    ""
]

description = \
    """
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "repository.qt"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
