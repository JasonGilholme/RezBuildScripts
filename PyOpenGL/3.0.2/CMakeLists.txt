CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezPipInstall)

set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(url "$ENV{REZ_REPO_PAYLOAD_DIR}/PyOpenGL/PyOpenGL-${version}.tar.gz")

rez_pip_install(
    PyOpenGL
    URL ${url}
)