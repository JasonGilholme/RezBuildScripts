#!/bin/bash

echo Running build in docker container!
echo =========================
export -p
echo =========================

export PATH=$PATH:/opt/cmake/bin

echo "About to source dev toolset"

source /opt/rh/devtoolset-6/enable

echo "Done that now!"

mkdir /docker_build/build
cd /docker_build/build
cmake -DCMAKE_INSTALL_PREFIX=/docker_build/out /docker_build
cmake --build .

chown -R $BUILD_UID:$BUILD_GID /docker_build/out
