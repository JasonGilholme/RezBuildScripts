name = "node"

version = "6.10.3"

authors = []

description = \
    """
    Node.js
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "repository.node"

def commands():
    env.PATH.append("{root}/bin")
