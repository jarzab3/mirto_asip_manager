import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mirto_asip_manager",
    version="1.0.2",
    author="Adam Jarzebak",
    author_email="adam@jarzebak.eu",
    description="Serial manager for Mirto robot services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jarzab3/mirto_asip_manager",
    packages=['mirto_asip_manager'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
    ),
)
