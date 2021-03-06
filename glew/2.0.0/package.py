name = "glew"

version = "2.0.0"

authors = [
    "Nigel Stewart"
]

description = \
    """
    OpenGL Extension Wrangler
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"],
    ["platform-linux", "arch-x86_64", "os-Ubuntu-17.04"]
]

uuid = "repository.glew"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.GLEW_INCLUDE_DIR = "{root}/include"
    env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
