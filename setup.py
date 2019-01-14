import os
from io import open
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()


setup(
    name="yauta",
    version='0.0.0.1',
    description="yet another unofficial tesla api",
    long_description=read('README.md'),
    url="https://github.com/thisisshi/yauta",
    install_requires=[
        "requests"
    ],
)

