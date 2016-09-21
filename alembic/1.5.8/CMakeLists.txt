CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(alembic_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_alembic alembic/${alembic_version}.tar.gz
    https://github.com/alembic/alembic/archive/${alembic_version}.tar.gz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

set(boost_root $ENV{REZ_BOOST_ROOT})
set(boost_inc $ENV{REZ_BOOST_ROOT}/include)
set(boost_lib $ENV{REZ_BOOST_ROOT}/lib)

set(ilmbase_root $ENV{REZ_ILMBASE_ROOT})
set(hdf_root $ENV{REZ_HDF5_ROOT})
set(glew_root $ENV{REZ_GLEW_ROOT})


ExternalProject_add(
    alembic
    URL ${url_alembic}
    PREFIX alembic
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND cmake
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DBUILD_SHARED_LIBS=ON
    -DGLEW_ROOT=${glew_root}
    -DGLEW_INCLUDE_DIR=${glew_root}/include
    -DGlew_INCLUDE_DIR=${glew_root}/include
    -DBOOST_ROOT=${boost_root}
    -DBOOST_INCLUDEDIR=${boost_inc}
    -DBOOST_LIBRARYDIR=${boost_lib}
    -DILMBASE_ROOT=${ilmbase_root}
    -DHDF5_ROOT=${hdf_root}
    -DUSE_PYALEMBIC=OFF
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j 4
    INSTALL_COMMAND "${install_cmd}"
)