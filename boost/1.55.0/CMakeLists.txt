CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(boost_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_boost boost/boost_1_55_0.tar.gz
    http://downloads.sourceforge.net/project/boost/boost/1.55.0/boost_1_55_0.tar.gz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    boost
    URL ${url_boost}
    PREFIX boost
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./bootstrap.sh
    INSTALL_COMMAND ""
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ./b2

     -q             # quits on first error
     -a             # always rebuilds targets
     -d1            # useful output verbosity
     -j ${ncpus}    # n jobs

     --prefix=${CMAKE_INSTALL_PREFIX}
     --exec-prefix=${CMAKE_INSTALL_PREFIX}
     --toolset=gcc

     link=static            # only produce static libs
     runtime-link=static    # link to static runtime lib
     variant=release        # create a release build

     cxxflags=-std=c++11    # we want to conform to c++11
     cxxflags=-fPIC         # position independent code
     cxxflags=-w            # don't show warnings

     ${install_cmd}

)
