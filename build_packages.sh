#!/bin/sh

set -e
cd $(dirname $0)


# VFX Platform Bundle
cd vfx_platform_bundle/2018
rez release


# VFX Platform
cd ../../vfx_platform/2018
rez release
rez env vfx_platform-2018 -- build_vfx_platform


# Python
cd ../../python/2.7.15
rez release


# Double Conversion
cd ../../double_conversion/1.1.5
rez release


# OpenEXR 
cd ../../openexr/2.2.0
rez release

# Qt
# cd ../../qt/5.6.3
# rez build -ic
