name = "alembic"

version = "1.5.8"

authors = [
    ""
]

description = \
    """
    """

build_requires = []

requires = [
	"boost-1.55",
	"ilmbase-2.2",
	"hdf5-1.8",
	"glew-1.10"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-14.04"]
]

uuid = "repository.alembic"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.ALEMBIC_INCLUDE_DIR = "{root}/include"
