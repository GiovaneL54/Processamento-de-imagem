#Codigo mais simples
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
with open("requiriments.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='packga_name',
    version='0.0.1',
    author= 'my_name',
    author_email='my_email',
    description='my short descriprion',
    long_description_contente_type='text/markdown',
    url='mygithub_reposiroty_project_link',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)