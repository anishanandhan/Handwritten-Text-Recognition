import os
from setuptools import setup, find_packages # type: ignore


DIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(DIR, "README.md")) as fh:
    long_description = fh.read()

with open(os.path.join(DIR, "requirements.txt")) as fh:
    requirements = fh.read().splitlines()


def get_version(initpath: str) -> str:
    """ Get from the init of the source code the version string

    Params:
        initpath (str): path to the init file of the python package relative to the setup file

    Returns:
        str: The version string in the form 0.0.1
    """

    path = os.path.join(os.path.dirname(__file__), initpath)

    with open(path, "r") as handle:
        for line in handle.read().splitlines():
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip("\"'")
        else:
            raise RuntimeError("Unable to find version string.")
        




