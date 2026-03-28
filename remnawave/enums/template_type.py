from enum import StrEnum


class TemplateType(StrEnum):
    STASH = "STASH"
    SINGBOX = "SINGBOX"
    SINGBOX_LEGACY = "SINGBOX_LEGACY"
    MIHOMO = "MIHOMO"
    XRAY_JSON = "XRAY_JSON"
    XRAY_BASE64 = "XRAY_BASE64"
    CLASH = "CLASH"
