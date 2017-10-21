name = "qt"

version = "4.8.6"

authors = [
    ""
]

description = \
    """
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"],
    ["platform-linux", "arch-x86_64", "os-Ubuntu-17.04"]
]

uuid = "repository.qt"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
