CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url mongoc/mongo-c-driver-${version}.tar.gz
    https://github.com/mongodb/mongo-c-driver/releases/download/${version}/mongo-c-driver-${version}.tar.gz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    mongoc
    URL ${url}
    PREFIX mongoc
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --exec-prefix=${CMAKE_INSTALL_PREFIX} --disable-automatic-init-and-cleanup
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus}
)
