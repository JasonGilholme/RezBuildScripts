CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

set(avrlibc_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_avrlibc avrlibc/avr-libc-${avrlibc_version}.tar.bz2
    http://download.savannah.gnu.org/releases/avr-libc/avr-libc-${avrlibc_version}.tar.bz2
)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install)
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    avrlibc
    URL ${url_avrlibc}
    PREFIX avrlibc
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --host=avr --prefix=${CMAKE_INSTALL_PREFIX} --exec-prefix=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j ${ncpus}
)
