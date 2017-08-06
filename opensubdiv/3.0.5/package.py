name = "opensubdiv"

version = "3.0.5"

authors = [
    "Pixar"
]

description = \
    """
    
    """

build_requires = [
    "ninja"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]
requires = [
	'glew-1',
	'glfw-3',
	'tbb-4.3',
	'ptex-2'
]

uuid = "repository.opensubdiv"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.OPENSUBDIV_INCLUDE_DIR = "{root}/include"
