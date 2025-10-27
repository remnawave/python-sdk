from enum import StrEnum

class OAuth2Provider(StrEnum):
    """OAuth2 Provider enum"""
    GITHUB = "github"
    POCKETID = "pocketid"
    YANDEX = "yandex"