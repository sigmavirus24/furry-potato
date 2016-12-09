"""Packaging logic."""
import os
import sys

import setuptools

_path_to_src = os.path.join(os.path.dirname(__file__), 'src')  # noqa: E402
sys.path.insert(0, _path_to_src)  # noqa: E402

import packageschema

requirements = [
    'attrs >= 16.3',
    'jsonschema >= 2.5.1',
    'pyyaml >= 3.12',
]

setuptools.setup(
    description='Schema generator and validator for Python packages',
    long_description='',
    package_dir={
        '': 'src',
    },
    packages=[
        'packageschema',
        'packageschema._cmd',
    ],
    install_requires=requirements,
    entry_points={
        'packageschema.commands': [],
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python 3.5',
        'Topic :: Software Development :: Libraries',
    ],
    **packageschema._metadata
)
