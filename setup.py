"""
setup.py
"""
from setuptools import setup, find_packages

setup (
    name='dicttools',
    version='0.1.0',
    author='Rodney Gomes',
    author_email='rodneygomes@gmail.com',
    url='',
    install_requires = [
                       ],
    tests_require = [
                    ],
    test_suite="test",
    keywords = [''],
    py_modules = ['dicttools'],
    packages = find_packages(exclude=['test']),
    license='Apache 2.0 License',
    description='',
    long_description=open('README.md').read(),
)
