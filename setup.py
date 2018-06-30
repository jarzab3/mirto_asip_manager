import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mirto_asip_manager",
    version="1.0",
    author="Adam Jarzebak",
    author_email="adam@jarzebak.eu",
    description="Serial manager for mirto robot services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jarzab3/mirto_asip_manager",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: linux2",
    ),
)