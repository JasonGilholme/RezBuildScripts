name = "ninja"

version = "1.7.2"

authors = [
    ""
]

description = \
    """
    Lightweight build system
    """

build_requires = ['rez_docker']

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**"]
    return [expand_requires(*requires)]

uuid = "repository.ninja"

def commands():
    env.PATH.append("{root}/bin")
