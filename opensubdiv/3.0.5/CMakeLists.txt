CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(opensubdiv_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_opensubdiv opensubdiv/v3_0_5.tar.gz
    https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v3_0_5.tar.gz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    opensubdiv
    URL ${url_opensubdiv}
    PREFIX opensubdiv
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake 
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    
    -DTBB_INCLUDE_DIR=$ENV{TBB_INCLUDE_DIR}
    -DTBB_LIBRARIES=$ENV{REZ_TBB_ROOT}/lib/release/libtbb.so
    -DTBB_INSTALL_DIR=$ENV{REZ_TBB_ROOT}
    
    -DGLFW_LOCATION=$ENV{REZ_GLFW_ROOT}
    -DPTEX_LOCATION=$ENV{REZ_PTEX_ROOT}
    -DGLEW_INCLUDE_DIR=$ENV{GLEW_INCLUDE_DIR}
    -DGLEW_LIBRARY=$ENV{REZ_GLEW_ROOT}/lib64/libGLEW.so

    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus}
)
