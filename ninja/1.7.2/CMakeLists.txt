CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url ninja/v${version}.tar.gz
    https://github.com/ninja-build/ninja/archive/v${version}.tar.gz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd mkdir ${CMAKE_INSTALL_PREFIX}/bin && cp ninja ${CMAKE_INSTALL_PREFIX}/bin/)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    ninja
    URL ${url}
    PREFIX ninja
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
    BUILD_COMMAND ../ninja/configure.py --bootstrap
)
