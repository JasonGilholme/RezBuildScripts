import os

import rez_docker


def build(source_path, build_path, install_path, targets):
    project_name = 'boost'
    remote_source_archive_url = 'http://downloads.sourceforge.net/project/boost/boost/%s/boost_%s.tar.gz' % (
        os.environ['REZ_BUILD_PROJECT_VERSION'], 
        os.environ['REZ_BUILD_PROJECT_VERSION'].replace('.', '_')
    )
    cmake_file = '%s/docker.CMakeLists.txt' % (os.environ['REZ_BUILD_SOURCE_PATH'],)

    rez_docker.build(
        project_name,
        remote_source_archive_url,
        cmake_file,
        install_path,
    )
