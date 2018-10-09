import os

import rez_docker


def build(source_path, build_path, install_path, targets):
    project_name = 'ninja'
    remote_source_archive_url = 'https://github.com/ninja-build/ninja/archive/v%s.tar.gz' % (os.environ['REZ_BUILD_PROJECT_VERSION'],)
    cmake_file = '%s/docker.CMakeLists.txt' % (os.environ['REZ_BUILD_SOURCE_PATH'],)

    rez_docker.build(
        project_name,
        remote_source_archive_url,
        cmake_file,
        install_path,
    )
