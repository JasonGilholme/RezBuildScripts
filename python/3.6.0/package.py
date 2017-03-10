name = "python"

version = "3.6.0"

authors = [
    "Guido van Rossum"
]

description = \
    """
    The Python programming language.
    """

build_requires = [
    #"gcc-4.8.2"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-16.04"]
]

tools = [
    "2to3",
    "idle",
    "pydoc",
    "python",
    "python2",
    "python2.7",
    "python2.7-config",
    "python2-config",
    "python-config",
    "smtpd.py"
]

uuid = "repository.python"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/lib/python3.6")

    if building:
        env.PYTHON_INCLUDE_DIR = "{root}/include/python3.6m"

        # only used to see libpythonX.X.a file
        env.LD_LIBRARY_PATH.append("{root}/lib")
