CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(shiboken_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_shiboken shiboken/${shiboken_version}.tar.gz
    https://github.com/pyside/Shiboken/archive/${shiboken_version}.tar.gz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    shiboken
    URL ${url_shiboken}
    PREFIX shiboken
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DQT_ROOT=${REZ_QT_ROOT} ../shiboken
    BUILD_IN_SOURCE 0
    #BINARY_DIR ${CMAKE_INSTALL_PREFIX}
    BUILD_COMMAND make -j ${ncpus}
    INSTALL_COMMAND "${install_cmd}"
)