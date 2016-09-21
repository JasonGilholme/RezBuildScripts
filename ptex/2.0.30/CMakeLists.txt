CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(ptex_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_ptex ptex/v${ptex_version}.zip
    http://github.com/wdas/ptex/archive/v${ptex_version}.zip
)

ExternalProject_add(
    ptex
    URL ${url_ptex}
    PREFIX ptex
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    INSTALL_COMMAND ""
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -C src INSTALLDIR=${CMAKE_INSTALL_PREFIX}
)
