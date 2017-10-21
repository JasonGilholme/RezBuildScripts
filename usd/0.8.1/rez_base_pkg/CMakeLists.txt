project(usd)

CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(ExternalProject)


ExternalProject_add(
    usd
    PREFIX usd

    DOWNLOAD_COMMAND ""

    CONFIGURE_COMMAND cmake

    # CCACHE
    -DCMAKE_CXX_COMPILER=ccache
    -DCMAKE_CXX_COMPILER_ARG1=g++
    -DCMAKE_C_COMPILER=ccache
    -DCMAKE_C_COMPILER_ARG1=gcc

    # BOOST
    -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}

    # TBB
    -DTBB_ROOT_DIR=$ENV{REZ_TBB_ROOT}
    -DTBB_tbb_LIBRARY_DEBUG=$ENV{REZ_TBB_ROOT}/lib/debug/
    -DTBB_tbb_LIBRARY_RELEASE=$ENV{REZ_TBB_ROOT}/lib/release/
    -DTBB_tbb_LIBRARY_DEBUG=$ENV{REZ_TBB_ROOT}/lib/debug/libtbb.so
    -DTBB_tbb_LIBRARY_RELEASE=$ENV{REZ_TBB_ROOT}/lib/release/libtbb.so

    # DOUBLE CONVERSION
    -DDOUBLE_CONVERSION_INCLUDE_DIR=$ENV{REZ_DOUBLE_CONVERSION_ROOT}/include
    -DDOUBLE_CONVERSION_LIBRARY=$ENV{REZ_DOUBLE_CONVERSION_ROOT}/lib/libdouble-conversion.so

    # OPENEXR
    -DOPENEXR_LOCATION=$ENV{REZ_OPENEXR_ROOT}
    -DOPENEXR_INCLUDE_DIR=$ENV{REZ_OPENEXR_ROOT}/include
    -DOPENEXR_LIBRARY_DIR=$ENV{REZ_OPENEXR_ROOT}/lib
    # because I have ilmbase and openexr as sepeerate packages
    -DOPENEXR_Half_LIBRARY=$ENV{REZ_ILMBASE_ROOT}/lib/libHalf.a
    #include_directories($ENV{REZ_ILMBASE_ROOT}/include)
    # gf libs mising OpenEXR namespace on includes
    #include_directories($ENV{REZ_ILMBASE_ROOT}/include/OpenEXR)

    #-DCMAKE_PREFIX_PATH=$ENV{REZ_ILMBASE_ROOT}/include/OpenEXR

    # OPENIMAGEIO
    -DOIIO_BASE_DIR=$ENV{REZ_OIIO_ROOT}

    # GLEW
    -DGLEW_LOCATION=$ENV{REZ_GLEW_ROOT}
    -DGLEW_LIBRARY=$ENV{REZ_GLEW_ROOT}/lib64/libGLEW.so

    # OPENSUBDIV
    -DOPENSUBDIV_ROOT_DIR=$ENV{REZ_OPENSUBDIV_ROOT}

    # PTEX
    -DPTEX_LOCATION=$ENV{REZ_PTEX_ROOT} 

    ${CMAKE_SOURCE_DIR}/../source/USD/

    BUILD_COMMAND make -j3
)