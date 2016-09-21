# -*- coding: utf-8 -*-

name = 'setuptools'

version = '27.3.0'

tools = [
    'easy_install'
]

build_requires = [
    #"gcc-4.8.2"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-14.04", "python-2.7"]
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")

uuid = 'repository.setuptools'
