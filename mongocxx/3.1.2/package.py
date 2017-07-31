name = "mongocxx"

version = "3.1.2"

authors = [
    "MongoDB"
]

description = \
    """
    MongoDB C++ driver
    """

requires = [
    "mongoc-1.5+",
    "boost-1.56+"
]

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "repository.mongocxx"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.MONGOCXX_INCLUDE_DIR = "{root}/include"
    env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
