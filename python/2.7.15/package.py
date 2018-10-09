name = "python"

version = "2.7.15.0"

authors = [
    "Guido van Rossum"
]

description = \
    """
    The Python programming language.
    """

private_build_requires = ['rez_docker']

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**"]
    return [expand_requires(*requires)]

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
    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/lib/python2.7")

    if building:
        env.PYTHON_INCLUDE_DIR = "{root}/include/python2.7"

        # only used to see libpythonX.X.a file
        env.LD_LIBRARY_PATH.append("{root}/lib")
