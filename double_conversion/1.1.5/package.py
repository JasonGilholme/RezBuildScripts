name = "double_conversion"

version = "1.1.5"

authors = [
    "Google"
]

description = \
    """
    Efficient binary-decimal and decimal-binary conversion routines for IEEE doubles.
    """

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**", "vfx_platform-2018"]
    return [expand_requires(*requires)]

uuid = "repository.double_conversion"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.DOUBLE_CONVERSION_INCLUDE_DIR = "{root}/include"
