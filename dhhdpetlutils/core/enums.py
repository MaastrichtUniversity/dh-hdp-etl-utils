"""This module stores the Enum classes"""

from enum import StrEnum


class ExtendedStrEnum(StrEnum):
    """Extended string enum class"""

    @classmethod
    def list(cls):
        """Return a list of StrEnum values"""
        return list(map(lambda c: c.value, cls))


class Nodenames(ExtendedStrEnum):
    """Enumerate the supported nodenames"""

    TEST = "test"
    MUMC = "mumc"
    ZIO = "zio"
    ENVIDA = "envida"
