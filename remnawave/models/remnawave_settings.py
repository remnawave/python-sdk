from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl


class PasskeySettings(BaseModel):
    """Passkey authentication settings"""
    enabled: bool
    rp_id: Optional[str] = Field(None, alias="rpId")
    origin: Optional[str] = None


class GitHubOAuth2Settings(BaseModel):
    """GitHub OAuth2 settings"""
    enabled: bool
    client_id: Optional[str] = Field(None, alias="clientId")
    client_secret: Optional[str] = Field(None, alias="clientSecret")
    allowed_emails: List[str] = Field(alias="allowedEmails")


class PocketIdOAuth2Settings(BaseModel):
    """PocketID OAuth2 settings"""
    enabled: bool
    client_id: Optional[str] = Field(None, alias="clientId")
    client_secret: Optional[str] = Field(None, alias="clientSecret")
    plain_domain: Optional[str] = Field(None, alias="plainDomain")
    allowed_emails: List[str] = Field(alias="allowedEmails")


class YandexOAuth2Settings(BaseModel):
    """Yandex OAuth2 settings"""
    enabled: bool
    client_id: Optional[str] = Field(None, alias="clientId")
    client_secret: Optional[str] = Field(None, alias="clientSecret")
    allowed_emails: List[str] = Field(alias="allowedEmails")


class OAuth2Settings(BaseModel):
    """OAuth2 authentication settings"""
    github: GitHubOAuth2Settings
    pocketid: PocketIdOAuth2Settings
    yandex: YandexOAuth2Settings


class TelegramAuthSettings(BaseModel):
    """Telegram authentication settings"""
    enabled: bool
    bot_token: Optional[str] = Field(None, alias="botToken")
    admin_ids: List[str] = Field(alias="adminIds")


class PasswordSettings(BaseModel):
    """Password authentication settings"""
    enabled: bool


class BrandingSettings(BaseModel):
    """Branding settings"""
    title: Optional[str] = None
    logo_url: Optional[HttpUrl] = Field(None, alias="logoUrl")


class RemnawaveSettingsData(BaseModel):
    """Remnawave settings data"""
    passkey_settings: Optional[PasskeySettings] = Field(None, alias="passkeySettings")
    oauth2_settings: Optional[OAuth2Settings] = Field(None, alias="oauth2Settings")
    tg_auth_settings: Optional[TelegramAuthSettings] = Field(None, alias="tgAuthSettings")
    password_settings: Optional[PasswordSettings] = Field(None, alias="passwordSettings")
    branding_settings: Optional[BrandingSettings] = Field(None, alias="brandingSettings")


class GetRemnawaveSettingsResponseDto(RemnawaveSettingsData):
    """Get Remnawave settings response"""
    pass


class UpdateRemnawaveSettingsRequestDto(BaseModel):
    """Update Remnawave settings request"""
    passkey_settings: Optional[PasskeySettings] = Field(None, serialization_alias="passkeySettings")
    oauth2_settings: Optional[OAuth2Settings] = Field(None, serialization_alias="oauth2Settings")
    tg_auth_settings: Optional[TelegramAuthSettings] = Field(None, serialization_alias="tgAuthSettings")
    password_settings: Optional[PasswordSettings] = Field(None, serialization_alias="passwordSettings")
    branding_settings: Optional[BrandingSettings] = Field(None, serialization_alias="brandingSettings")


class UpdateRemnawaveSettingsResponseDto(RemnawaveSettingsData):
    """Update Remnawave settings response"""
    pass