CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(googletest_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_googletest googletest/release-${googletest_version}.tar.gz
    https://github.com/google/googletest/archive/release-${googletest_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    googletest
    URL ${url_googletest}
    PREFIX googletest
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)
