name = "PySideTools"

version = "0.2.15"

authors = [
    ""
]

description = \
    """
    
    """

requires = [
    "shiboken-1.2",
    "PySide-1.2"
]   

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-14.04", "python-2.7"]
]

uuid = "repository.PySideTools"

def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
