#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

# import setuptools
from distutils.core import setup

with open('README.md', mode = 'r') as readme_file:
    readme = readme_file.read().decode('utf-8')

# get the dependencies and installs
with io.open(op.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
if platform.system() != "Windows":
    install_requires.append('pygdal==' + PYGDAL_VERSION)
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]

setup(
    name="dingpy",
    version="0.0.13",
    author="Tina Bu",
    author_email="tina.hongbu@gmail.com",
    description="plays ding sounds",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    url="https://github.com/Tina-Bu/dingpy/",
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
    ],
    install_requires=install_requires,
    dependency_links=dependency_links,
    license="MIT license",
    include_package_data=True,
    keywords='dingpy',
    name='dingpy',
    packages=find_packages(include=['dingpy']),
    setup_requires=setup_requirements,
    url='https://github.com/Tina-Bu/dingpy',
    zip_safe=False,
)


