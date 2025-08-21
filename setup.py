from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ml-doguser",
    version="0.1",
    author="Dousery",
    packages=find_packages(),  # src olmadan, ana dizindeki tüm __init__.py klasörlerini bulur
    install_requires=requirements,
    python_requires=">=3.8",
)