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


class LogAuditTrailTopics(ExtendedStrEnum):
    """Enumerate the supported topics for all logs"""

    EXTRACT = "Extract"
    LOAD = "Load"
    TRANSFORM = "Transform"


class LogLevelTags(ExtendedStrEnum):
    """Enumerate the supported topics for audit trail logs"""

    INFO = "INFO"
    AUDIT_TRAIL = "AUDIT_TRAIL"
    WARNING = "WARNING"
    ERROR = "ERROR"
