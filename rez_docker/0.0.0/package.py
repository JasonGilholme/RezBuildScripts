name = "rez_docker"

version = "0.0.0"

authors = [
    "jason.gilholme"
]

private_build_requires = ["python"]

description = "Python utils to build rez packages in a docker container"

uuid = "repository.rez_docker"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")
