from enum import StrEnum

class ResponseRuleOperator(StrEnum):
    """Response rule logical operators"""
    AND = "AND"
    OR = "OR"


class ResponseRuleConditionOperator(StrEnum):
    """Response rule condition operators"""
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    CONTAINS = "CONTAINS"
    NOT_CONTAINS = "NOT_CONTAINS"
    STARTS_WITH = "STARTS_WITH"
    NOT_STARTS_WITH = "NOT_STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    NOT_ENDS_WITH = "NOT_ENDS_WITH"
    REGEX = "REGEX"
    NOT_REGEX = "NOT_REGEX"


class ResponseType(StrEnum):
    """Response types for subscription rules"""
    XRAY_JSON = "XRAY_JSON"
    XRAY_BASE64 = "XRAY_BASE64"
    MIHOMO = "MIHOMO"
    STASH = "STASH"
    CLASH = "CLASH"
    SINGBOX = "SINGBOX"
    BROWSER = "BROWSER"
    BLOCK = "BLOCK"
    STATUS_CODE_404 = "STATUS_CODE_404"
    STATUS_CODE_451 = "STATUS_CODE_451"
    SOCKET_DROP = "SOCKET_DROP"


class ResponseRuleVersion(StrEnum):
    """Response rules config version"""
    V1 = "1"