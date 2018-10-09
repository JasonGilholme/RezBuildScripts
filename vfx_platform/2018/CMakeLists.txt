cmake_minimum_required(VERSION 2.8)

include(RezBuild)

file(GLOB_RECURSE py_files "python/*.py")
rez_install_python(
    py
    FILES ${py_files}
    DESTINATION .
)

file(GLOB_RECURSE docker_files "docker/*")
rez_install_files(
    ${docker_files}
    DESTINATION .
    EXECUTABLE
)

file(GLOB bin_files "bin/*")
rez_install_files(
    ${bin_files}
    DESTINATION .
    EXECUTABLE
)
