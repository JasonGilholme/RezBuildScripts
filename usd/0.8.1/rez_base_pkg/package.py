name = "usd"

version = "0.7.2.0"

authors = [
    "Pixar"
]

description = \
    """
    Universal Scene Description
    """

requires = [
    "boost-1.61",
    "tbb-2017.6",
    "double_conversion-1.1",
    "openexr-2.2",
    "oiio-1.7",
    "glew-1.10",
    "opensubdiv-3",
    "ptex-2.0",
    "PyOpenGL-3",
    "PySide",
    "PySideTools",
]

build_requires = [
    "ccache"
]

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**", "vfx_platform-2018"]
    return [expand_requires(*requires)]

uuid = "usd"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python")
