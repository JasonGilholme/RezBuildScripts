name = "glfw"

version = "3.2.1"

authors = [
    ""
]

description = \
    """
    GL 
    """

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**", "vfx_platform-2018"]
    return [expand_requires(*requires)]

uuid = "repository.glfw"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.GLFW_INCLUDE_DIR = "{root}/include"
