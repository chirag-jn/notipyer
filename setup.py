from setuptools import setup, find_packages

from notipyer import __version__ as version

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='notipyer',
    version=version,
    description='Notification Triggers for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Chirag Jain',
    url='https://github.com/chirag-jn/notipyer',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
