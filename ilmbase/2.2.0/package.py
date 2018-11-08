name = "ilmbase"

version = "2.2.0"

authors = [
    "ILM"
]

description = \
    """
    Utility libraries from ILM used by OpenEXR.
    """

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**", "vfx_platform-2018"]
    return [expand_requires(*requires)]

uuid = "repository.ilmbase"

def commands():
    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
        env.ILMBASE_INCLUDE_DIR = "{root}/include"

        # static libs only, hence build-time only
        env.LD_LIBRARY_PATH.append("{root}/lib")
