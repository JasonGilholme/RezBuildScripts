name = "blender"

version = "2.78c"

authors = [
    ""
]

description = \
    """
    Blender
    """

requires = [
    "oiio",
    "glew"
]

build_requires = [
    "openexr"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "repository.blender"

def commands():
    env.PATH.append("{root}/bin")
