"""This contains all schema related bits of packageschema.

This serves a dual-purpose:

    1. It has the versioned schema that validates the ``packageschema.yaml``
       files.

    2. It reads and parses the ``packageschema.yaml`` files.

As a result, there are a few classes hidden in here.
"""
import os.path

import attr
import jsonschema
import yaml

from packageschema import exceptions
from packageschema import package

SCHEMATA_VERSIONS = [
    '2016.12',
]

Version201612 = {
    'type': 'object',
    'required': [
        'schema',
        'package',
    ],
    'properties': {
        'schema': {
            'type': 'object',
            'required': [
                'version',
            ],
            'properties': {
                'version': {
                    'type': 'string',
                    'enum': SCHEMATA_VERSIONS,
                },
            },
        },
        'package': {
            'type': 'object',
            'required': [
                'name',
                'version',
                'module_names',
                'exports',
            ],
            'properties': {
                'name': {
                    'type': 'string',
                },
                'version': {
                    'type': 'string',
                },
                'module_names': {
                    'type': 'array',
                    'minItems': 1,
                    'items': {
                        'type': 'string',
                    },
                },
                'exports': {
                    'type': 'array',
                    'minItems': 1,
                    'items': {
                        'type': 'string',
                    },
                },
            },
        },
    },
}

Version201612Validator = jsonschema.validators.Draft4Validator(Version201612)


@attr.s
class Schema:
    schema_data = attr.ib(
        validator=attr.validators.instance_of(dict),
        repr=False,
    )
    version = attr.ib(init=False, default=None)
    validator = attr.ib(
        init=False,
        repr=False,
        validator=attr.validators.instance_of(jsonschema.validators.Draft4Validator),
    )
    validators = {
        '2016.12': Version201612Validator,
    }

    def __attrs_post_init__(self):
        self.version = self.schema_data['version']
        self.validator = self.validators.get(self.version)
        if self.validator is None:
            raise exceptions.InvalidSchemaVersion(self.version)

    def validate(self, packageschema):
        """Use the loaded schema to apply JSON Schema validation."""
        self.validator.validate(packageschema)


@attr.s
class PackageSchema:
    """This handles and represents the parsed ``packageschema.yaml`` file."""

    schema = attr.ib(validator=attr.validators.instance_of(Schema))
    package = attr.ib(validator=attr.validators.instance_of(package.Package))

    @classmethod
    def from_file(cls, path):
        """Read the file specified by ``path`` and parse it.

        :param str path:
            Absolute path to the file to read.
        :returns:
            Parsed package schema file.
        :rtype:
            PackageSchema
        """
        if not os.path.abspath(path):
            raise ValueError(
                "You are required to pass an absolute path to the file to "
                "parse but you provided a relative path ({!r})".format(path)
            )

        if not os.path.isfile(path):
            raise exceptions.FileDoesNotExist(path)

        with open(path, 'r') as packageschema_file:
            filedata = yaml.safe_load(packageschema_file)

        schema = Schema(filedata['schema'])
        schema.validate(filedata)
        return cls(
            schema=schema,
            package=package.Package(**filedata['package']),
        )

    def validate(self):
        """Validate using the declared schema version."""
        self.schema.validate(self.package)
