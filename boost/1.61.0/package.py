name = "boost"

version = "1.61.0"

authors = [
    "boost.org"
]

description = \
    """
    Peer-reviewed portable C++ source libraries.
    """

build_requires = []

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**", "os-**"]
    return [expand_requires(*requires)]

uuid = "repository.boost"

def commands():
    if building:
        # cmake FindPackage env vars
        env.BOOST_ROOT = "{root}"
        env.BOOST_INCLUDEDIR = "{root}/include"
