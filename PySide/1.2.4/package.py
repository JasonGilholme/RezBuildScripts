name = "PySide"

version = "1.2.4"

authors = [
    ""
]

description = \
    """
    
    """

requires = [
	"qt-4.8.6",
	"pip",
	"setuptools",
	"shiboken"
]

build_requires = []

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-14.04", "python-2.7"]
]

uuid = "repository.PySide"

def commands():
    env.PYTHONPATH.append('{root}/python')
