import os
import subprocess


def build(package_name, remote_source_archive_url, cmake_file, install_dir, rez_repo_dir=None, build_uid=None, build_gid=None):
    rez_repo_dir = rez_repo_dir or os.environ.get("REZ_REPO_PAYLOAD_DIR")
    if not rez_repo_dir:
        raise Exception("Please provide rez_repo_dir argument or set the REZ_REPO_PAYLOAD_DIR environment variable!")

    build_uid = build_uid or os.environ.get("REZ_BUILD_DOCKER_UID", 1000)
    build_gid = build_gid or os.environ.get("REZ_BUILD_DOCKER_GID", 1000)

    #
    # Determine if the source archive has already been downloaded
    #
    source_archive_name = os.path.basename(remote_source_archive_url)
    local_source_archive_dir = os.path.join(rez_repo_dir, package_name)
    local_source_archive_url = os.path.join(rez_repo_dir, package_name, source_archive_name)

    if not os.path.isfile(local_source_archive_url):
        source_archive_url = remote_source_archive_url
    else:
        source_archive_url = os.path.join("/docker_build/src", package_name, source_archive_name)

    #
    # Build the command to run
    #
    cmd = "docker run --privileged --rm -t "

    # Add env vars
    cmd += "-e CMAKE_URL=%s " % (source_archive_url,)
    cmd += "-e CMAKE_DOWNLOAD_DIR=%s " % (local_source_archive_dir,)
    cmd += "-e BUILD_UID=%s " % (build_uid,)
    cmd += "-e BUILD_GID=%s " % (build_gid,)

    # Add volumes for build input and output
    cmd += "-v %s:/docker_build/src " % (rez_repo_dir,)
    cmd += "-v %s:/docker_build/out " % (install_dir,)
    cmd += "-v %s:/docker_build/CMakeLists.txt " % (cmake_file,)

    # Add rez package volumes
    rez_package_dirs = os.environ.get('REZ_PACKAGES_PATH', '').split(':')
    for pkg_dir in rez_package_dirs:
        print 'Adding rez package path:', pkg_dir
        cmd += "-v %s:%s " % (pkg_dir, pkg_dir)
    
    cmd += "-v %s:/rez_context.sh " % (os.environ['REZ_CONTEXT_FILE'],)

    # The docker image to run
    cmd += "vfx_platform:2018"
    print '[BUILD CMD]', cmd
    cmd = cmd.split()

    #
    # Run the subprocess
    #
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while True:
        output = proc.stdout.readline()
        if output == '' and proc.poll() is not None:
            break
        if output:
            print output.strip()

    if proc.poll() != 0:
        #TODO: get error from subproc
        raise Exception("Error while running build in docker container!")
