name = "usd_maya"

version = "0.7.2.0"

authors = [
    "Pixar"
]

description = \
    """
    Universal Scene Description
    """

requires = [
    "app_maya-2017",
    
    "boost-1.55",
    #"tbb-4.3",
    "double_conversion-1.1",
    "openexr-2.2",
    "oiio-1.5",
    "glew-1.10",
    "opensubdiv-3",
    "ptex-2.0",
    "PyOpenGL-3",
    #"PySide",
    #"PySideTools",
]

build_requires = [
    "ccache"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-14.04"]
]

uuid = "usd_maya"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python")
