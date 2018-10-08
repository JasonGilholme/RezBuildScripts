CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(ExternalProject)

set(rez_version $ENV{REZ_BUILD_PROJECT_VERSION})
set(remote_url http://www.python.org/ftp/python/${rez_version}/Python-${rez_version}.tgz)

ExternalProject_add(
    python
    SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    INSTALL_COMMAND ""
    BUILD_COMMAND ${CMAKE_CURRENT_LIST_DIR}/../../docker_build
        python
        ${remote_url}
        ${CMAKE_CURRENT_LIST_DIR}/docker.CMakeLists.txt
        ${CMAKE_INSTALL_PREFIX}
)

install(CODE "")

