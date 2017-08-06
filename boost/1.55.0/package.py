name = "boost"

version = "1.55.0"

authors = [
    "boost.org"
]

description = \
    """
    Peer-reviewed portable C++ source libraries.
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04", "python-2.7"],
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04", "python-3.5"]
]

uuid = "repository.boost"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

    # cmake FindPackage env vars
    env.BOOST_ROOT = "{root}"
    env.BOOST_INCLUDEDIR = "{root}/include"
