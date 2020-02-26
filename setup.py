import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jqc",
    version="0.0.1",
    author="Jake Blackmore",
    author_email="j.a.blackmore@durham.ac.uk",
    description="A small package for standardising plots using jqc styles",
    long_description=long_description,
    include_package_data = True,
    packages=['jqc'],
    install_requires=['matplotlib'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)