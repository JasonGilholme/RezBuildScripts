CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(tbb_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_tbb tbb/tbb-${tbb_version}.tgz
    https://www.threadingbuildingblocks.org/sites/default/files/software_releases/source/tbb43_20150611oss_src.tgz
)

ExternalProject_add(
    tbb
    URL ${url_tbb}
    PREFIX tbb
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    INSTALL_COMMAND python ${CMAKE_CURRENT_LIST_DIR}/install.py ./ ${CMAKE_INSTALL_PREFIX}
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus}
)
