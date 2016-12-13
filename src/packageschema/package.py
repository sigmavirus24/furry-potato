"""This defines what a "Package" actually is in packageschema.

.. autoclass:: Package
"""
import attr
from packaging import utils as pkg_utils
from packaging import version

from packageschema import _attrs


@attr.s
class Package:
    """The object used to interact with a specific package."""

    name = attr.ib(convert=pkg_utils.canonicalize_name)
    version = attr.ib(convert=version.Version)
    module_names = attr.ib(
        validator=_attrs.list_of(attr.validators.instance_of(str))
    )
    exports = attr.ib(
        validator=_attrs.list_of(attr.validators.instance_of(str))
    )
