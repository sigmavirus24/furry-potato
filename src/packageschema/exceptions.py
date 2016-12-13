"""Collected exceptions raised by packageschema.

.. autoclass:: FileDoesNotExist
"""
import attr


class PackageSchemaException(Exception):
    pass


@attr.s
class FileDoesNotExist(PackageSchemaException):
    path = attr.ib()

    def __str__(self):
        return "File {!r} does not exist".format(self.path)


@attr.s
class InvalidSchemaVersion(PackageSchemaException):
    version = attr.ib()

    def __str__(self):
        return "Version {!r} is not a known schema".format(self.version)
