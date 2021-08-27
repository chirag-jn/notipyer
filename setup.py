from setuptools import setup, find_packages

from notipyer import __version__ as version
from notipyer import __url__ as url
from notipyer import __name__ as name
from notipyer import __short_desc__ as short_desc


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=name,
    version=version,
    description=short_desc,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Chirag Jain',
    url=url,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
