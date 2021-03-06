import os

import vfx_platform


def build(source_path, build_path, install_path, targets):
    project_name = 'python'
    version_number = os.environ['REZ_BUILD_PROJECT_VERSION'].rsplit('.', 1)[0]
    remote_source_archive_url = 'http://www.python.org/ftp/python/%s/Python-%s.tgz' % (version_number, version_number)
    cmake_file = '%s/docker.CMakeLists.txt' % (os.environ['REZ_BUILD_SOURCE_PATH'],)

    vfx_platform.build(
        project_name,
        remote_source_archive_url,
        cmake_file,
        install_path,
    )
