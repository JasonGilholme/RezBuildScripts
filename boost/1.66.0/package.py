name = "boost"

version = "1.66.0"

authors = [
    "boost.org"
]

description = \
    """
    Peer-reviewed portable C++ source libraries.
    """

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**", "python-2.7.15"]
    return [expand_requires(*requires)]

uuid = "repository.boost"

def commands():
    if building:
        # cmake FindPackage env vars
        env.BOOST_ROOT = "{root}"
        env.BOOST_INCLUDEDIR = "{root}/include"
