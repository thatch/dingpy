# import setuptools
from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dingpy",
    version="0.0.13",
    author="Tina Bu",
    author_email="tina.hongbu@gmail.com",
    description="Included audio file to package with MANIFEST.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tina-Bu/dingpy/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)