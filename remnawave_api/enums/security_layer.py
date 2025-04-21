from enum import StrEnum


class SecurityLayer(StrEnum):
    DEFAULT = "DEFAULT"
    TLS = "TLS"
    NONE = "NONE"
