import os

import rez_docker


def build(source_path, build_path, install_path, targets):
    project_name = 'qt'
    remote_source_archive_url = 'http://download.qt.io/archive/qt/%s/%s/single/qt-everywhere-opensource-src-%s.tar.xz' % (
        os.environ['REZ_BUILD_PROJECT_VERSION'].rsplit('.', 1)[0],
        os.environ['REZ_BUILD_PROJECT_VERSION'], 
        os.environ['REZ_BUILD_PROJECT_VERSION'], 
    )
    cmake_file = '%s/docker.CMakeLists.txt' % (os.environ['REZ_BUILD_SOURCE_PATH'],)

    rez_docker.build(
        project_name,
        remote_source_archive_url,
        cmake_file,
        install_path,
    )
