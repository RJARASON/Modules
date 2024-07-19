from setuptools import setup,find_packages

setup(
    name="kmmodules"
    ,
    version="0.1.0",
    author="Kodjo Messie",
    author_email="kodjomessie@gmail.com",
    description="My Python Works.",
    packages=find_packages(),
    install_requires=[
        "some_package>=1.0.0",
    ],
    command_packages="command_packages= pip install kmmodules",
)