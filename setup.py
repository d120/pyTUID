import os
from setuptools import find_packages, setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pyTUID',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='AGPL-3.0',  # example license
    description='Django app for authentication via TUID (CAS)',
    #long_description=README,
    #url='https://www.example.com/',
    author='Fabian Franke',
    author_email='ffranke@d120.de',
    install_requires=[
        'python-cas',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)