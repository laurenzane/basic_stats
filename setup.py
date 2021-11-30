from setuptools import setup

setup(
    name = "basic_stats",
    version = "0.0.1",
    author = "Lauren Zane",
    package_dir={"basic_stats"},
    packages=['mean'],
    install_requires=['matplotlib','numpy'],
)
