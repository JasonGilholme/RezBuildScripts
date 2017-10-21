name = "app_maya"

version = "2018.0.0"

authors = [
    "Autodesk"
]

description = \
    """
    
    """

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-14.04"],
    ["platform-linux", "arch-x86_64", "os-Ubuntu-17.04"]
]

uuid = "repository.app_maya"

def commands():
    env.PATH.append("{root}/ext/bin")
    env.LD_LIBRARY_PATH = "{root}/ext/lib"
