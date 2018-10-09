name = "openexr"

version = "2.2.0"

authors = [
    "ILM"
]

description = \
    """
    ILM's high dynamic-range (HDR) image file format library.
    """

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**", "vfx_platform-2018"]
    return [expand_requires(*requires)]

tools = [
    "exrenvmap",
    "exrheader",
    "exrmakepreview",
    "exrmaketiled",
    "exrmultipart",
    "exrmultiview",
    "exrstdattr"
]

uuid = "repository.openexr"

def commands():
    env.REZ_ILMBASE_ROOT = "{root}"
    env.ILMBASE_INCLUDE_DIR = "{root}/include"

    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
    env.OPENEXR_INCLUDE_DIR = "{root}/include"
