name = "opensubdiv"

version = "3.0.5"

authors = [
    "Pixar"
]

description = ""

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**", "vfx_platform-2018"]
    return [expand_requires(*requires)]

requires = [
    'glew-1',
    'glfw-3',
    'tbb-2017.6',
    # 'ptex-2'
]

uuid = "repository.opensubdiv"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.OPENSUBDIV_INCLUDE_DIR = "{root}/include"
