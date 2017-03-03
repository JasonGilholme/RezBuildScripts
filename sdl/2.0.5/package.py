name = "sdl"

version = "2.0.5"

authors = [
	""
]

description = \
    """
	Simple Direct Media
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

uuid = "repository.sdl"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.SDL_INCLUDE_DIR = "{root}/include"
