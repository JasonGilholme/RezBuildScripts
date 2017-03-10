name = "oiio"

version = "1.7.11"

authors = [
    "Larry Gritz"
]

description = \
    """
    OpenImageIO is a library for reading and writing images, and a bunch of related classes, utilities, and applications.
    """

build_requires = []

requires = [
	"openexr-2.2",
	"glew-1",
	"boost-1.63"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "repository.oiio"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.OIIO_INCLUDE_DIR = "{root}/include"
    env.PYTHONPATH.append("{root}/lib/python/site-packages")
