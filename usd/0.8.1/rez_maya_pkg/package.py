name = "usd_maya"

version = "0.8.1"

authors = [
    "Pixar"
]

description = \
    """
    Universal Scene Description
    """

requires = [
    "boost-1.55",
    #"tbb-4.3",
    "double_conversion-1.1",
    "openexr-2.2",
    "oiio-1.5",
    "glew-1.10",
    "opensubdiv-3",
    "ptex-2.0",
    # "PyOpenGL-3",
    #"PySide",
    #"PySideTools",
]

build_requires = [
    "ccache"
]

variants = [
    # Ubuntu 14.04
    ["platform-linux", "arch-x86_64", "os-Ubuntu-14.04", "app_maya-2018.0.0"],

    # Ubuntu 17.04
    ["platform-linux", "arch-x86_64", "os-Ubuntu-17.04", "app_maya-2018.0.0"]
]

uuid = "usd_maya"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib/python")

    env.PXR_INSTALL_LOCATION.append("{root}")
    env.PXR_PLUGINPATH_NAME.append("{root}/plugin")
    env.PXR_PLUGINPATH_NAME.append("{root}/share/usd/plugins")

    env.MAYA_PLUG_IN_PATH.append("{root}/third_party/maya/plugin")
    env.LD_LIBRARY_PATH.append("{root}/third_party/maya/lib")
    env.MAYA_SCRIPT_PATH.append("{root}/third_party/maya/share/usd/plugins/usdMaya/resources")
    env.MAYA_VP2_DEVICE_OVERRIDE = "VirtualDeviceGL"
    env.MAYA_VP2_USE_VP1_SELECTION = "1"
