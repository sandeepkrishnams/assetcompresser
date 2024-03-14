"""Python setup.py for assetcompresser package"""

import io
import os

from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("assetcompresser", "VERSION")
    '0.0.1'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="assetcompresser",
    version=read("assetcompresser", "VERSION"),
    description="AssetCompresser: Streamline Your Uploads with Efficient Compression",
    url="https://github.com/sandeepkrishnams/assetcompresser",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Sandeep MS",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["assetcompresser = assetcompresser.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
