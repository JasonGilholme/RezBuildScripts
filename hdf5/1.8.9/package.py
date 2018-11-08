name = "hdf5"

version = "1.8.9"

authors = [
    "The HDF Group"
]

description = \
    """
    Data model, library, and file format for storing and managing data.
    """

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**", "vfx_platform-2018"]
    return [expand_requires(*requires)]

tools = [
    "gif2h5"
    "h52gif"
    "h5cc"
    "h5copy"
    "h5debug"
    "h5diff"
    "h5dump"
    "h5import"
    "h5jam"
    "h5ls"
    "h5mkgrp"
    "h5perf_serial"
    "h5redeploy"
    "h5repack"
    "h5repart"
    "h5stat"
    "h5unjam"
]

uuid = "repository.hdf5"

def commands():
    env.PATH.append("{root}/bin")

    if building:
        env.HDF5_INCLUDE_DIR = "{root}/include"

        # static libs
        env.LD_LIBRARY_PATH.append("{root}/lib")
