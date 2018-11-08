name = "glew"

version = "1.10.0"

authors = [
    "Nigel Stewart"
]

description = \
    """
    OpenGL Extension Wrangler
    """

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**", "vfx_platform-2018"]
    return [expand_requires(*requires)]

uuid = "repository.glew"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.GLEW_INCLUDE_DIR = "{root}/include"
    env.PKG_CONFIG_PATH.append("{root}/lib64/pkgconfig")
