"""This has :mod:`attr` related code in it."""
import attr


@attr.s(repr=False, slots=True)
class _ListOf:
    validator = attr.ib()

    def __call__(self, instance, attr, value):
        if not isinstance(value, list):
            raise TypeError(
                "'{}' must be a list but got {!r}".format(
                    attr.name, value.__class__,
                )
            )

        for item in value:
            self.validator(instance, attr, item)

def list_of(validator):
    return _ListOf(validator)
