from enum import StrEnum


class ClientType(StrEnum):
    STASH = "stash"
    SINGBOX = "singbox"
    SINGBOX_LEGACY = "singbox_legacy"
    MIHOMO = "mihomo"
    JSON = "json"
    CLASH = "clash"
