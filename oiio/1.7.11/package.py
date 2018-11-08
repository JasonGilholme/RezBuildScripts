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
    "boost-1.61",
    "python-2.7",
]

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**", "vfx_platform-2018"]
    return [expand_requires(*requires)]

uuid = "repository.oiio"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.OIIO_INCLUDE_DIR = "{root}/include"
    env.PYTHONPATH.append("{root}/lib/python/site-packages")
