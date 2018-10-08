CMAKE_MINIMUM_REQUIRED(VERSION 2.8)


include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)


set(rez_version $ENV{REZ_BUILD_PROJECT_VERSION})
string(REPLACE "." "_" boost_filename_version ${rez_version})

set(repo_dir $ENV{REZ_REPO_PAYLOAD_DIR}/boost)
set(local_url ${repo_dir}/boost_${boost_filename_version}.tar.gz)
set(remote_url http://downloads.sourceforge.net/project/boost/boost/${rez_version}/boost_${boost_filename_version}.tar.gz)

if (EXISTS ${local_url})
    set(url ${local_url})
    set(dl_dir "")
else()
    set(url ${remote_url})
    set(dl_dir ${repo_dir})
endif()


ExternalProject_add(
    boost
    URL ${url}
    DOWNLOAD_DIR ${dl_dir}
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

     cxxflags=-std=c++14    # we want to conform to c++11
     cxxflags=-fPIC         # position independent code
     cxxflags=-w            # don't show warnings

     install
 )

install(CODE "")

