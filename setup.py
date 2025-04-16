# coding: utf-8

"""
    BoldSign API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Contact: support@boldsign.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import sys
from setuptools import setup, find_packages  # noqa: H301
from pathlib import Path

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "boldsign"
VERSION = "1.0.0b9"

# Check if a version was passed via command-line arguments
if "--version" in sys.argv:
    version_index = sys.argv.index("--version") + 1
    if version_index < len(sys.argv):
        VERSION = sys.argv[version_index]
        sys.argv = [arg for arg in sys.argv if arg not in ("--version", VERSION)]

PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

this_directory = Path(__file__).parent
content = (this_directory / "README.md").read_text()
split_marker = "## Documentation for API Endpoints"
long_description = content.split(split_marker)[0]

setup(
    name=NAME,
    version=VERSION,
    description="BoldSign API",
    author="BoldSign",
    author_email="support@boldsign.com",
    url="https://github.com/boldsign/boldsign-python-sdk",
    keywords=["boldsign", "api", "sdk", "BoldSign API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={"boldsign": ["py.typed"]},
)
