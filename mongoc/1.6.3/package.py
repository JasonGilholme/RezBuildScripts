name = "mongoc"

version = "1.6.3"

authors = [
    "MongoDB"
]

description = \
    """
    MongoDB C driver
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "repository.mongoc"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.MONGOC_INCLUDE_DIR = "{root}/include"
    env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
