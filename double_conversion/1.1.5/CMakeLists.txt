CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(double_conversion_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_double_conversion double_conversion/v${double_conversion_version}.tar.gz
    https://github.com/google/double-conversion/archive/v${double_conversion_version}.tar.gz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd ninja install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    double_conversion
    URL ${url_double_conversion}
    PREFIX double_conversion
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake -GNinja -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DBUILD_SHARED_LIBS=ON
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ninja
)
