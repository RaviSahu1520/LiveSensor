from setuptools import find_packages, setup

def get_requirements() -> list[str]:
    requirement_list: list[str] = []
    return requirement_list

setup(
    name='sensor',
    version='0.0.1',
    author='ravi',
    author_email='ravi786modi@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)
