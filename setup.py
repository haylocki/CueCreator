from setuptools import find_packages, setup

setup(
    name="CueCreator",
    version="1.0.0",
    description="Create cue file for a directory containing audio files",
    author="Ian Haylock",
    author_email="haylocki@yahoo.co.uk",
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=[
        "PyQt6>=6.0",
        "mutagen>=1.45.1",
    ],
)
