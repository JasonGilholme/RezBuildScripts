name = "qt"

version = "5.6.3"

authors = [
    ""
]

description = \
    """
    """

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**", "vfx_platform-2018"]
    return [expand_requires(*requires)]

uuid = "repository.qt"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
