CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(blender_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_blender blender/blender-${blender_version}.tar.gz
    https://github.com/glfw/glfw/archive/${glfw_version}.tar.gz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    blender
    URL ${url_blender}
    PREFIX blender
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} 
    -DGLEW_INCLUDE_DIR=$ENV{GLEW_INCLUDE_DIR}
    -DGLEW_LIBRARY=$ENV{GLEW_LIBRARY}
    -DWITH_SYSTEM_GLEW=OFF
    -DOPENIMAGEIO_INCLUDE_DIR=$ENV{OPENIMAGEIO_INCLUDE_DIR}
    -DOPENIMAGEIO_LIBRARY=$ENV{OPENIMAGEIO_LIBRARY} ../blender
    INSTALL_COMMAND "${install_cmd}"
    BUILD_COMMAND make -j ${ncpus}
)
