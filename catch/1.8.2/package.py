name = "catch"

version = "1.8.2"

authors = [
    ""
]

description = \
    """
    OpenGL Extension Wrangler
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "repository.glew"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.GLEW_INCLUDE_DIR = "{root}/include"
    env.PKG_CONFIG_PATH.append("{root}/lib64/pkgconfig")
