import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="perpyu",
    version="0.0.1",
    author="Ashutosh Sathe",
    author_email="satheab16.mech@coep.ac.in",
    description="Personal Python Utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashutoshbsathe/perpyu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)