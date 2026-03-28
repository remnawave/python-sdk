from enum import StrEnum

class OAuth2Provider(StrEnum):
    """OAuth2 Provider enum"""
    TELEGRAM = "telegram"
    GITHUB = "github"
    POCKETID = "pocketid"
    YANDEX = "yandex"
    KEYCLOAK = "keycloak"
    GENERIC = "generic"