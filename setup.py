# SPDX-FileCopyrightText: Copyright contributors to the Software Quality Assurance as a Service (SQAaaS) project <sqaaas@ibergrid.eu>
# SPDX-FileContributor: Pablo Orviz <orviz@ifca.unican.es>
#
# SPDX-License-Identifier: GPL-3.0-only

# coding: utf-8

from setuptools import find_packages, setup

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
]

setup(
    name="sqaaas_api_utils",
    version="1.0.0",
    description="SQAaaS API Utils",
    author="Pablo Orviz",
    author_email="orviz@ifca.unican.es",
    url="https://github.com/eosc-synergy/sqaaas-api-utils",
    keywords=["SQAaaS API"],
    install_requires=[
        "requests"
    ],
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Frequently used utils to programmatically interact with the SQAaaS API.
    """,
    setuptools_git_versioning={
        "enabled": True,
    },
    setup_requires=["setuptools-git-versioning>=2.0,<3"],
)
