CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(ccache_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_ccache ccache/ccache-${ccache_version}.tar.gz
    https://www.samba.org/ftp/ccache/ccache-3.3.3.tar.gz
)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    ccache
    URL ${url_ccache}
    PREFIX ccache
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --exec-prefix=${CMAKE_INSTALL_PREFIX} --prefix=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus}
)
