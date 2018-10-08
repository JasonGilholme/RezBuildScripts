CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(ExternalProject)

set(rez_version $ENV{REZ_BUILD_PROJECT_VERSION})
set(remote_url http://download.qt.io/archive/qt/5.6/${rez_version}/single/qt-everywhere-opensource-src-${rez_version}.tar.xz)

ExternalProject_add(
    qt
    SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    INSTALL_COMMAND ""
    BUILD_COMMAND ${CMAKE_CURRENT_LIST_DIR}/../../docker_build
        qt
        ${remote_url}
        ${CMAKE_CURRENT_LIST_DIR}/docker.CMakeLists.txt
        ${CMAKE_INSTALL_PREFIX}
)

install(CODE "")

