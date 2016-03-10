import PyATMM

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the RpythonEADME file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PyATMM',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=PyATMM.__version__,

    description='Implementation of the transfer matrix method',
    long_description=long_description,

    url='https://github.com/kitchenknif/PyTMM',

    author=PyATMM.__author__,
    author_email='pavel.a.dmitriev@gmail.com',

    # license=PyATMM.__license__,

    classifiers=[

        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['numpy', 'scipy'],

    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
)