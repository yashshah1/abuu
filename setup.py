import pathlib
from setuptools import setup, find_packages

import abuu

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="abuu",
    version=abuu.__version__,
    description="ABUU - Another Bunch of Usefull Utils",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/yashshah1/abuu",
    author="Yash Shah",
    author_email="yashshah1234@gmail.com",
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    	"pandas>=1.0.0",
    	"scikit-learn>=0.22.1"
    ],
)
