name = "gsl"

version = "2.3"

authors = []

description = \
    """
    GNU Scientific Library
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-14.04"]
]

uuid = "repository.gsl"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.GSL_INCLUDE_DIR = "{root}/include"
