name = "vfx_platform"

version = "2018"

description = "Containerised build environment for the vfx reference platform"

authors = [
    "jason.gilholme"
]

private_build_requires = ["python"]

uuid = "repository.vfx_platform"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")
