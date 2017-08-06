CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url mongocxx/mongo-cxx-driver-r${version}.tar.gz
    https://github.com/mongodb/mongo-cxx-driver/releases/download/${version}/mongo-cxx-driver-${version}.tar.gz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd ninja install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    mongocxx
    URL ${url}
    PREFIX mongocxx
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake -GNinja -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DBSONCXX_POLY_USE_BOOST=1 ../mongocxx
    INSTALL_COMMAND "${install_cmd}"
    BUILD_COMMAND ninja
)
