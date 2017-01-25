name = "PyOpenGL"

version = "3.0.2"

authors = [
    ""
]

description = \
    """
    
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-14.04"]
]

uuid = "repository.PyOpenGL"

def commands():
    env.PYTHONPATH.append("{root}/python")
