import os

import vfx_platform


def build(source_path, build_path, install_path, targets):
    project_name = 'ilmbase'
    version_number = os.environ['REZ_BUILD_PROJECT_VERSION']
    remote_source_archive_url = 'http://download.savannah.nongnu.org/releases/openexr/ilmbase-%s.tar.gz' % (version_number,)
    cmake_file = '%s/docker.CMakeLists.txt' % (os.environ['REZ_BUILD_SOURCE_PATH'],)

    vfx_platform.build(
        project_name,
        remote_source_archive_url,
        cmake_file,
        install_path,
    )

    project_name = 'openexr'
    version_number = os.environ['REZ_BUILD_PROJECT_VERSION']
    remote_source_archive_url = 'http://download.savannah.nongnu.org/releases/openexr/openexr-%s.tar.gz' % (version_number,)
    cmake_file = '%s/docker.CMakeLists.txt' % (os.environ['REZ_BUILD_SOURCE_PATH'],)

    vfx_platform.build(
        project_name,
        remote_source_archive_url,
        cmake_file,
        install_path,
    )
