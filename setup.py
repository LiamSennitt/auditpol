from setuptools import setup, find_packages


with open('README.md', 'r') as file:
    long_description = file.read()


setup(
    name='auditpol',
    version='1.0.0',
    author='Liam Sennitt',
    description='Windows Audit Policy parser and emitter for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LiamSennitt/auditpol',
    packages=find_packages()
)
