name = "ninja"

version = "1.7.2"

authors = [
    ""
]

description = \
    """
    Lightweight build system
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "repository.ninja"

def commands():
    env.PATH.append("{root}/bin")
