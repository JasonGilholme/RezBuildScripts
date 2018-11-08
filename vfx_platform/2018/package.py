name = "vfx_platform"

version = "2018.0.2"

description = "Containerised build environment for the vfx reference platform"

authors = [
    "jason.gilholme"
]

private_build_requires = ["python-2.7.15"]

uuid = "repository.vfx_platform"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")
