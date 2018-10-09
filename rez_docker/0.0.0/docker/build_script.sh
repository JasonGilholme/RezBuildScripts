#!/bin/bash

echo "source rez context"
source /rez_context.sh 
echo "done with that"
export PATH=$PATH:/opt/cmake/bin

source /opt/rh/devtoolset-6/enable


echo Running build in docker container!
echo =========================
export -p
echo =========================

mkdir /docker_build/build
cd /docker_build/build
cmake -DCMAKE_INSTALL_PREFIX=/docker_build/out /docker_build
cmake --build .

chown -R $BUILD_UID:$BUILD_GID /docker_build/out
