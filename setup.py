#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygalaxy",
    version="0.1.8",
    author="patrickxu",
    author_email="patrickxu@wiatec.com",
    description="common package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/patrickxu1986/pygalaxy",
    project_urls={
        "Bug Tracker": "https://github.com/patrickxu1986/pygalaxy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

# deploy project to pypi
# pip3 install --upgrade build
# python3 -m build
# pip3 install --upgrade twine
# python3 -m twine upload --repository pypi dist/*
