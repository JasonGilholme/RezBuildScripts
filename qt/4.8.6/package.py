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
    ["platform-linux", "arch-x86_64", "os-Ubuntu-14.04"]
]

uuid = "repository.qt"

def commands():
	pass
    #env.LD_LIBRARY_PATH.append("{root}/lib")
    #env.DOUBLE_CONVERSION_INCLUDE_DIR = "{root}/include"
