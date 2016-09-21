name = "glfw"

version = "3.2.1"

authors = [
    ""
]

description = \
    """
    GL 
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-14.04"]
]

uuid = "repository.glfw"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.GLFW_INCLUDE_DIR = "{root}/include"
