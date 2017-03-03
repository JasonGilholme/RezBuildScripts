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
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04", "python-2.7"]
]

uuid = "repository.PySide"

def commands():
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
