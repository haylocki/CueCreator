from setuptools import setup, find_packages

setup(
    name="CueCreator",
    version="1.0.0",
    description="Create cue file for a directory containing audio files",
    author="Ian Haylock",
    author_email="haylocki@yahoo.co.uk",
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=[
        "pyqt5>=5.15",
        "mutagen>=1.45.1",
    ],
)
