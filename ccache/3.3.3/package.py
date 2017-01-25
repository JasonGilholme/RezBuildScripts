name = "ccache"

version = "3.3.3"

authors = [
    "Andrew 'Tridge' Tridgell",
    "Joel Rosdahl"
]

description = \
    """
    Compiler Cache
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-14.04"]
]

uuid = "repository.ccache"

def commands():
    env.PATH.append("{root}/bin")
