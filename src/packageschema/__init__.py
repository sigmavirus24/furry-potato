"""The Package Schema library and package."""

__all__ = tuple()

_version_data = {
    'major': 0,
    'minor': 1,
    'patch': 0,
    'pre_release': None,
}

__version__ = '{major}.{minor}.{patch}'.format(**_version_data)
if _version_data['pre_release'] is not None:
    __version__ += '.' + _version_data['pre_release']

__build__ = int(
    '0x{major:02}{minor:02}{patch:02}'.format(**_version_data),
    base=16
)


_metadata = {
    'author': 'Ian Cordasco',
    'author_email': 'graffatcolmingov@gmail.com',
    'version': __version__,
    'license': 'BSD 3-Clause License or Apache License, Version 2.0',
    'url': 'https://github.com/sigmavirus24/packageschema',
}
