CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(oiio_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_oiio oiio/Release-${oiio_version}.tar.gz
    https://github.com/OpenImageIO/oiio/archive/Release-${oiio_version}.tar.gz
)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    oiio
    URL ${url_oiio}
    PREFIX oiio
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake .
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DILMBASE_CUSTOM_INCLUDE_DIR=$ENV{ILMBASE_INCLUDE_DIR} 
    -DILMBASE_CUSTOM_LIB_DIR=$ENV{REZ_ILMBASE_ROOT}/lib
    -DOPENEXR_CUSTOM_INCLUDE_DIR=$ENV{OPENEXR_INCLUDE_DIR} 
    -DOPENEXR_CUSTOM_LIB_DIR=$ENV{REZ_OPENEXR_ROOT}/lib
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus}
)
