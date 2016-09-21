name = 'pip'

version = '8.1.2'

tools = [
    'pip',
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-14.04", "python-2.7"]
]

requires = [
    'setuptools'
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = '2c43d523-92bb-4f2b-b812-70202f54d3f1'
