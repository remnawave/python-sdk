from .api_tokens_management import (
    CreateApiTokenRequestDto,
    CreateApiTokenResponseDto,
    DeleteApiTokenResponseDto,
    FindAllApiTokensResponseDto,
)
from .auth import (
    GetStatusResponseDto,
    LoginRequestDto,
    LoginResponseDto,
    RegisterRequestDto,
    RegisterResponseDto,
    StatusResponseDto,  # Legacy alias
    TelegramCallbackRequestDto,
    TelegramCallbackResponseDto,
    LoginTelegramRequestDto,  # Legacy alias
    OAuth2AuthorizeRequestDto,
    OAuth2AuthorizeResponseDto,
    OAuth2CallbackRequestDto,
    OAuth2CallbackResponseDto,
    VerifyPasskeyAuthenticationRequestDto,
    VerifyPasskeyAuthenticationResponseDto,
    GetPasskeyAuthenticationOptionsResponseDto,
)
from .bandwidthstats import (
    GetNodeUserUsageByRangeResponseDto,
    GetNodesRealtimeUsageResponseDto,
    GetNodesUsageByRangeResponseDto,
    GetUserUsageByRangeResponseDto,
    NodeRealtimeUsageResponseDto,
    NodeUsageResponseDto,
    NodesRealtimeUsageResponseDto,  # Legacy alias
    NodesUsageResponseDto,  # Legacy alias
    GetLegacyStatsUserUsageResponseDto,
    GetLegacyStatsNodesUsersUsageResponseDto,
    GetStatsNodesRealtimeUsageResponseDto,
    GetStatsNodesUsageResponseDto,
    GetStatsNodeUsersUsageResponseDto,
    GetStatsUserUsageResponseDto,

    # Data Models
    LegacyUserUsageItem,
    LegacyNodeUserUsageItem,
    NodeRealtimeUsageItem,
    TopNodeItem,
    TopUserItem,
    NodeSeriesItem,
    StatsNodesUsageData,
    StatsNodeUsersUsageData,
    StatsUserUsageData,
)
from .config_profiles import (
    ConfigProfileDto,
    CreateConfigProfileRequestDto,
    CreateConfigProfileResponseDto,
    DeleteConfigProfileResponseDto,
    GetAllConfigProfilesResponseDto,
    GetAllConfigProfilesResponsePaginated,
    GetAllInboundsResponseDto,
    GetConfigProfileByUuidResponseDto,
    GetInboundsByProfileUuidResponseDto,
    InboundDto,
    NodesProfileDto,
    UpdateConfigProfileRequestDto,
    UpdateConfigProfileResponseDto,
)
from .hosts import (
    CreateHostInboundData,
    CreateHostRequestDto,
    CreateHostResponseDto,
    DeleteHostResponseDto,
    GetAllHostsResponseDto,
    GetOneHostResponseDto,
    HostInboundData,
    HostResponseDto,
    HostsResponseDto,  # Legacy alias
    ReorderHostItem,
    ReorderHostRequestDto,
    ReorderHostResponseDto,
    UpdateHostRequestDto,
    UpdateHostResponseDto,
    GetAllHostTagsResponseDto,
)
from .hosts_bulk_actions import (
    BulkDeleteHostsResponseDto,
    BulkDisableHostsResponseDto,
    BulkEnableHostsResponseDto,
    SetInboundToManyHostsRequestDto,
    SetInboundToManyHostsResponseDto,
    SetPortToManyHostsResponseDto,
    SetPortToManyHostsRequestDto
)
from .hwid import (
    CreateHWIDUser,  # Legacy alias
    CreateUserHwidDeviceRequestDto,
    CreateUserHwidDeviceResponseDto,
    DeleteUserHwidDeviceRequestDto,
    DeleteUserHwidDeviceResponseDto,
    GetUserHwidDevicesResponseDto,
    HWIDDeleteRequest,  # Legacy alias
    HWIDUserResponseDto,  # Legacy alias
    HWIDUserResponseDtoList,  # Legacy alias
    GetHwidStatisticsResponseDto,
    DeleteUserAllHwidDeviceRequestDto,
    GetTopUsersByHwidDevicesResponseDto,
    TopUserByHwidDevicesDto,
    TopUsersByHwidDevicesData,
)
from .inbounds import (
    AllInboundsData,
    FullInboundResponseDto,
    FullInboundStatistic,
    FullInboundsResponseDto,
    GetAllInboundsResponseDto,
    GetFullInboundsResponseDto,
    GetInboundsByProfileUuidResponseDto,
    GetInboundsResponseDto,
    InboundResponseDto,
    InboundsByProfileData,
    InboundsResponseDto,  # Legacy alias
)
from .inbounds_bulk_actions import (
    AddInboundToNodesResponseDto,
    AddInboundToUsersResponseDto,
    RemoveInboundFromNodesResponseDto,
    RemoveInboundFromUsersResponseDto,
)
from .infra_billing import (
    CreateInfraBillingHistoryRecordRequestDto,
    CreateInfraBillingHistoryRecordResponseDto, 
    CreateInfraBillingNodeRequestDto,
    CreateInfraBillingNodeResponseDto,
    CreateInfraProviderRequestDto,
    CreateInfraProviderResponseDto,
    DeleteInfraBillingHistoryRecordByUuidResponseDto,  
    DeleteInfraBillingNodeByUuidResponseDto,  # ПЕРЕИМЕНОВАНА (было DeleteInfraBillingNodeResponseDto)
    DeleteInfraProviderByUuidResponseDto,  # ПЕРЕИМЕНОВАНА (было DeleteInfraProviderResponseDto)
    GetInfraBillingHistoryRecordsResponseDto,  # ПЕРЕИМЕНОВАНА (было GetAllInfraBillingHistoryResponseDto)
    GetInfraBillingNodesResponseDto,  # ПЕРЕИМЕНОВАНА (было GetAllInfraBillingNodesResponseDto)
    GetInfraProvidersResponseDto,  # ПЕРЕИМЕНОВАНА (было GetAllInfraProvidersResponseDto)
    GetInfraBillingHistoryByUuidResponseDto,
    GetInfraBillingNodeByUuidResponseDto,
    GetInfraProviderByUuidResponseDto,
    InfraBillingHistoryDto,
    InfraBillingNodeDto,
    InfraProviderDto,
    NodeDto,
    UpdateInfraBillingNodeRequestDto,
    UpdateInfraBillingNodeResponseDto,
    UpdateInfraProviderRequestDto,
    UpdateInfraProviderResponseDto,
    DeleteInfraBillingNodeResponseDto,  # LEGACY
    DeleteInfraProviderResponseDto,  # LEGACY
    GetAllInfraBillingHistoryResponseDto,  # LEGACY
    GetAllInfraBillingNodesResponseDto,  # LEGACY
    GetAllInfraProvidersResponseDto,  # LEGACY
)
from .internal_squads import (
    AddUsersToInternalSquadRequestDto,
    AddUsersToInternalSquadResponseDto,
    CreateInternalSquadRequestDto,
    CreateInternalSquadResponseDto,
    DeleteInternalSquadResponseDto,
    DeleteUsersFromInternalSquadRequestDto,
    DeleteUsersFromInternalSquadResponseDto,
    GetAllInternalSquadsResponseDto,
    GetInternalSquadByUuidResponseDto,
    InternalSquadDto,
    UpdateInternalSquadRequestDto,
    UpdateInternalSquadResponseDto,
    GetInternalSquadAccessibleNodesResponseDto,
)
from .keygen import GetPubKeyResponseDto, PubKeyResponseDto  # Legacy alias
from .nodes import (
    CreateNodeRequestDto,
    CreateNodeResponseDto,
    DeleteNodeResponseDto,
    DisableNodeResponseDto,
    EnableNodeResponseDto,
    ExcludedInbounds,
    GetAllNodesResponseDto,
    GetOneNodeResponseDto,
    NodeConfigProfileDto,
    NodeConfigProfileRequestDto,
    NodeResponseDto,
    NodesResponseDto,  # Legacy alias
    ReorderNodeRequestDto,
    ReorderNodeResponseDto,
    RestartAllNodesResponseDto,
    RestartNodeResponseDto,
    UpdateNodeRequestDto,
    UpdateNodeResponseDto,
    RestartAllNodesRequestDto, # Legacy alias,
    RestartAllNodesRequestBodyDto,
    ResetNodeTrafficRequestDto,
    ResetNodeTrafficResponseDto
)
from .nodes_usage_history import (
    GetNodeUserUsageByRangeResponseDto,
    GetNodesUsageByRangeResponseDto,
    GetUserAccessibleNodesResponseDto,
    NodeInfoDto,
    NodeUsageDto,
    UserUsageDto,
)
from .subscription import (
    GetAllSubscriptionsResponseDto,
    GetSubscriptionByUsernameResponseDto,
    GetSubscriptionInfoResponseDto,
    SubscriptionInfoResponseDto,  # Legacy alias
    UserSubscription,
    GetRawSubscriptionByShortUuidResponseDto,
    RawSettings,
    GetSubscriptionByShortUUIDResponseDto,
    GetSubscriptionByUUIDResponseDto,
)
from .subscriptions_settings import (
    GetSubscriptionSettingsResponseDto,
    ResponseModificationHeader,
    ResponseModifications,
    ResponseRule,
    ResponseRuleCondition,
    ResponseRules,
    SubscriptionSettingsResponseDto,
    UpdateSubscriptionSettingsRequestDto,
    UpdateSubscriptionSettingsResponseDto,
    CustomRemarksDto,
    HwidSettingsDto,
    # Backward compatibility aliases
    CustomRemarks,
    HwidSettings,
)
from .subscriptions_template import (
    CreateSubscriptionTemplateRequestDto,
    CreateSubscriptionTemplateResponseDto,
    DeleteSubscriptionTemplateResponseDto,
    GetTemplatesResponseDto,
    TemplateInfoDto,
    GetTemplateResponseDto,
    TemplateResponseDto,
    UpdateTemplateRequestDto,
    UpdateTemplateResponseDto,
)
from .system import (
    BandwidthStatistic,
    BandwidthStatisticResponseDto,
    CPUStatistic,
    GetBandwidthStatsResponseDto,
    GetNodesStatisticsResponseDto,
    GetRemnawaveHealthResponseDto,
    GetStatsResponseDto,
    MemoryStatistic,
    NodeStatistic,
    NodesStatisticResponseDto,
    OnlineStatistic,
    StatisticResponseDto,
    StatusCounts,
    UsersStatistic,
    GetNodesMetricsResponseDto,
    GetX25519KeyPairResponseDto, 
    X25519KeyPair,
    DebugSrrMatcherRequestDto,
    DebugSrrMatcherResponseDto,
    EncryptHappCryptoLinkRequestDto,
    EncryptHappCryptoLinkResponseDto,
)
from .users import (
    # Request DTOs
    CreateUserRequestDto,
    UpdateUserRequestDto,
    RevokeUserRequestDto,
    
    # Response DTOs - Single User
    CreateUserResponseDto,
    UpdateUserResponseDto,
    GetUserByUuidResponseDto,
    GetUserByShortUuidResponseDto,
    GetUserByUsernameResponseDto,
    GetUserByIdResponseDto,
    DisableUserResponseDto,
    EnableUserResponseDto,
    ResetUserTrafficResponseDto,
    RevokeUserSubscriptionResponseDto,
    ActivateAllInboundsResponseDto,
    
    # Response DTOs - Collections
    GetAllUsersResponseDto,
    GetAllTagsResponseDto,
    GetUserSubscriptionRequestHistoryResponseDto,
    
    # Response DTOs - Arrays (RootModel)
    TelegramUserResponseDto,
    EmailUserResponseDto,
    TagUserResponseDto,
    
    # Other Response DTOs
    DeleteUserResponseDto,
    
    # Base DTOs
    UserResponseDto,
    UsersResponseDto,
    TagsResponseDto,
    SubscriptionRequestsResponseData,
    
    # Data DTOs
    UserTrafficDto,
    ActiveInternalSquadDto,
    SubscriptionRequestRecord,
    HappCrypto,
    UserActiveInboundsDto,
    UserLastConnectedNodeDto,

    # Alias
    GetSubscriptionRequestsResponseDto,
)

from .users_bulk_actions import (
    BulkAllExtendExpirationDateRequestDto, 
    BulkAllExtendExpirationDateResponseDto, 
    BulkAllResetTrafficUsersResponseDto,
    BulkAllUpdateUsersRequestDto,
    BulkAllUpdateUsersResponseDto,
    BulkDeleteUsersByStatusRequestDto, 
    BulkDeleteUsersByStatusResponseDto, 
    BulkDeleteUsersRequestDto, 
    BulkDeleteUsersResponseDto, 
    BulkEventResponseData, 
    BulkExtendExpirationDateRequestDto, 
    BulkExtendExpirationDateResponseDto, 
    BulkResetTrafficUsersRequestDto, 
    BulkResetTrafficUsersResponseDto, 
    BulkResponseData, 
    BulkResponseDto,
    BulkRevokeUsersSubscriptionRequestDto, 
    BulkRevokeUsersSubscriptionResponseDto, 
    BulkUpdateUsersInternalSquadsRequestDto,
    BulkUpdateUsersRequestDto, 
    BulkUpdateUsersResponseDto, 
    BulkUpdateUsersSquadsRequestDto, 
    BulkUpdateUsersSquadsResponseDto, 
    TagStr, 
    UpdateUserFields,
)
from .users_stats import UserUsageByRange, UserUsageByRangeResponseDto
from .xray_config import (
    ConfigResponseDto,  # Legacy alias
    GetConfigResponseDto,
    UpdateConfigRequestDto,
    UpdateConfigResponseDto,
)
from .subscription_request_history import (
    GetAllSubscriptionRequestHistoryResponseDto,
    GetSubscriptionRequestHistoryStatsResponseDto,
    SubscriptionRequestHistoryRecord,
    SubscriptionRequestHistoryData,
    AppStatItem,
    HourlyRequestStat,
    SubscriptionRequestHistoryStatsData
)
from .webhook import (
    UserEventDto, 
    UserHwidDeviceEventDto,
    HwidUserDeviceDto,
    LastConnectedNodeDto,
    InternalSquadDto,
    BaseUserDto,
    UserDto,
    NodeDto,
    ConfigProfileInboundDto,
    InfraProviderDto,
    LoginAttemptDto,
    ServiceEventDto,
    NodeEventDto,
    CustomErrorEventDto,
    CrmEventDto,
    WebhookPayloadDto,
    UserTrafficDto
)
from .passkeys import (
    DeletePasskeyRequestDto,
    DeletePasskeyResponseDto,
    GetAllPasskeysResponseDto,
    GetPasskeyRegistrationOptionsResponseDto,
    PasskeyDto,
    VerifyPasskeyRegistrationRequestDto,
    VerifyPasskeyRegistrationResponseDto,
)
from .external_squads import (
    AddUsersToExternalSquadResponseDto,
    CreateExternalSquadRequestDto,
    CreateExternalSquadResponseDto,
    DeleteExternalSquadResponseDto,
    ExternalSquadDto,
    ExternalSquadInfoDto,
    ExternalSquadSubscriptionSettingsDto,
    ExternalSquadTemplateDto,
    GetExternalSquadByUuidResponseDto,
    GetExternalSquadsResponseDto,
    RemoveUsersFromExternalSquadResponseDto,
    TemplateType,
    UpdateExternalSquadRequestDto,
    UpdateExternalSquadResponseDto,
)
from .snippets import (
    CreateSnippetRequestDto,
    CreateSnippetResponseDto,
    DeleteSnippetRequestDto,
    DeleteSnippetResponseDto,
    GetSnippetsResponseDto,
    SnippetItem,
    SnippetsData,
    UpdateSnippetRequestDto,
    UpdateSnippetResponseDto,
)
from .remnawave_settings import (
    BrandingSettings,
    GetRemnawaveSettingsResponseDto,
    GitHubOAuth2Settings,
    OAuth2Settings,
    PasskeySettings,
    PasswordSettings,
    PocketIdOAuth2Settings,
    RemnawaveSettingsData,
    TelegramAuthSettings,
    UpdateRemnawaveSettingsRequestDto,
    UpdateRemnawaveSettingsResponseDto,
    YandexOAuth2Settings,
)
from .subscription_page import (
    CloneSubscriptionPageConfigRequestDto,
    CloneSubscriptionPageConfigResponseDto,
    CreateSubscriptionPageConfigRequestDto,
    CreateSubscriptionPageConfigResponseDto,
    DeleteSubscriptionPageConfigResponseDto,
    GetSubscriptionPageConfigResponseDto,
    GetSubscriptionPageConfigsResponseDto,
    ReorderSubscriptionPageConfigItem,
    ReorderSubscriptionPageConfigsRequestDto,
    ReorderSubscriptionPageConfigsResponseDto,
    SubscriptionPageConfigDto,
    UpdateSubscriptionPageConfigRequestDto,
    UpdateSubscriptionPageConfigResponseDto,
)

__all__ = [
    # Auth models
    "GetStatusResponseDto",
    "LoginRequestDto",
    "LoginResponseDto",
    "RegisterRequestDto",
    "RegisterResponseDto",
    "StatusResponseDto",  # Legacy alias
    "TelegramCallbackRequestDto",
    "TelegramCallbackResponseDto",
    "LoginTelegramRequestDto",  # Legacy alias
    "OAuth2AuthorizeRequestDto",
    "OAuth2AuthorizeResponseDto",
    "OAuth2CallbackRequestDto",
    "OAuth2CallbackResponseDto",
    "VerifyPasskeyAuthenticationRequestDto",
    "VerifyPasskeyAuthenticationResponseDto",
    "GetPasskeyAuthenticationOptionsResponseDto",
    # Nodes models
    "CreateNodeRequestDto",
    "CreateNodeResponseDto",
    "DeleteNodeResponseDto",
    "DisableNodeResponseDto",
    "EnableNodeResponseDto",
    "ExcludedInbounds",
    "GetAllNodesResponseDto",
    "GetOneNodeResponseDto",
    "NodeResponseDto",
    "NodesResponseDto",  # Legacy alias
    "ReorderNodeRequestDto",
    "ReorderNodeResponseDto",
    "RestartAllNodesResponseDto",
    "RestartNodeResponseDto",
    "UpdateNodeRequestDto",
    "UpdateNodeResponseDto",
    "NodeConfigProfileDto",
    "NodeConfigProfileRequestDto",
    "RestartAllNodesRequestDto",  # Legacy alias
    "RestartAllNodesRequestBodyDto",
    "ResetNodeTrafficRequestDto",
    "ResetNodeTrafficResponseDto",
    # Hosts models
    "CreateHostRequestDto",
    "CreateHostResponseDto",
    "DeleteHostResponseDto",
    "GetAllHostsResponseDto",
    "GetOneHostResponseDto",
    "HostResponseDto",
    "HostsResponseDto",  # Legacy alias
    "ReorderHostRequestDto",
    "ReorderHostResponseDto",
    "UpdateHostRequestDto",
    "UpdateHostResponseDto",
    "GetAllHostTagsResponseDto",
    "CreateHostInboundData",
    "HostInboundData",
    "ReorderHostItem",
    # Inbounds models
    "AllInboundsData",
    "FullInboundResponseDto",
    "FullInboundStatistic",
    "FullInboundsResponseDto",
    "GetFullInboundsResponseDto",
    "GetInboundsResponseDto",
    "InboundResponseDto",
    "InboundsResponseDto",  # Legacy alias
    "GetInternalSquadAccessibleNodesResponseDto",
    "InboundsByProfileData",
    # Keygen models
    "GetPubKeyResponseDto",
    "PubKeyResponseDto",  # Legacy alias
    # Subscription models
    "GetAllSubscriptionsResponseDto",
    "GetSubscriptionByUsernameResponseDto",
    "GetSubscriptionByShortUUIDResponseDto",
    "GetSubscriptionByUUIDResponseDto",
    "GetSubscriptionInfoResponseDto",
    "SubscriptionInfoResponseDto",  # Legacy alias
    "UserSubscription",
    "GetRawSubscriptionByShortUuidResponseDto",
    "RawSettings",
    # Subscription settings models
    "GetSubscriptionSettingsResponseDto",
    "SubscriptionSettingsResponseDto",
    "UpdateSubscriptionSettingsRequestDto",
    "CustomRemarksDto",
    "HwidSettingsDto",
    # Backward compatibility aliases
    "CustomRemarks",
    "HwidSettings",
    "UpdateSubscriptionSettingsResponseDto",
    "ResponseModificationHeader",
    "ResponseModifications",
    "ResponseRule",
    "ResponseRuleCondition",
    "ResponseRules",
    # Subscription template models
    "GetTemplateResponseDto",
    "TemplateResponseDto",
    "UpdateTemplateRequestDto",
    "UpdateTemplateResponseDto",
    "CreateSubscriptionTemplateRequestDto",
    "CreateSubscriptionTemplateResponseDto",
    "DeleteSubscriptionTemplateResponseDto",
    "GetTemplatesResponseDto",
    "TemplateInfoDto",
    # System models
    "BandwidthStatistic",
    "BandwidthStatisticResponseDto",
    "CPUStatistic",
    "GetBandwidthStatsResponseDto",
    "GetNodesStatisticsResponseDto",
    "GetRemnawaveHealthResponseDto",
    "GetStatsResponseDto",
    "MemoryStatistic",
    "NodeStatistic",
    "NodesStatisticResponseDto",
    "OnlineStatistic",
    "StatisticResponseDto",
    "StatusCounts",
    "UsersStatistic",
    "GetNodesMetricsResponseDto",
    "GetX25519KeyPairResponseDto",
    "X25519KeyPair",
    "DebugSrrMatcherRequestDto",
    "DebugSrrMatcherResponseDto",
    "EncryptHappCryptoLinkRequestDto",
    "EncryptHappCryptoLinkResponseDto",
    # XRay config models
    "ConfigResponseDto",  # Legacy alias
    "GetConfigResponseDto",
    "UpdateConfigRequestDto",
    "UpdateConfigResponseDto",
    # HWID models
    "CreateHWIDUser",  # Legacy alias
    "CreateUserHwidDeviceRequestDto",
    "CreateUserHwidDeviceResponseDto",
    "DeleteUserHwidDeviceRequestDto",
    "DeleteUserHwidDeviceResponseDto",
    "GetUserHwidDevicesResponseDto",
    "HWIDDeleteRequest",  # Legacy alias
    "HWIDUserResponseDto",  # Legacy alias
    "HWIDUserResponseDtoList",  # Legacy alias
    "GetHwidStatisticsResponseDto",
    "DeleteUserAllHwidDeviceRequestDto",
    "GetTopUsersByHwidDevicesResponseDto",
    "TopUserByHwidDevicesDto",
    "TopUsersByHwidDevicesData",
    # Bandwidth stats models
    "GetNodeUserUsageByRangeResponseDto",
    "GetNodesRealtimeUsageResponseDto",
    "GetNodesUsageByRangeResponseDto",
    "GetUserUsageByRangeResponseDto",
    "NodeRealtimeUsageResponseDto",
    "NodeUsageResponseDto",
    "NodesRealtimeUsageResponseDto",  # Legacy alias
    "NodesUsageResponseDto",  # Legacy alias
    "GetLegacyStatsUserUsageResponseDto",
    "GetLegacyStatsNodesUsersUsageResponseDto",
    "GetStatsNodesRealtimeUsageResponseDto",
    "GetStatsNodesUsageResponseDto",
    "GetStatsNodeUsersUsageResponseDto",
    "GetStatsUserUsageResponseDto",
    "LegacyUserUsageItem",
    "LegacyNodeUserUsageItem",
    "NodeRealtimeUsageItem",
    "TopNodeItem",
    "TopUserItem",
    "NodeSeriesItem",
    "StatsNodesUsageData",
    "StatsNodeUsersUsageData",
    "StatsUserUsageData",
    # API Tokens models
    "CreateApiTokenRequestDto",
    "CreateApiTokenResponseDto",
    "DeleteApiTokenResponseDto",
    "FindAllApiTokensResponseDto",
    # Inbound bulk actions models
    "AddInboundToNodesResponseDto",
    "AddInboundToUsersResponseDto",
    "RemoveInboundFromNodesResponseDto",
    "RemoveInboundFromUsersResponseDto",
    # Host bulk actions models
    "BulkDeleteHostsResponseDto",
    "BulkDisableHostsResponseDto",
    "BulkEnableHostsResponseDto",
    "SetInboundToManyHostsRequestDto",
    "SetInboundToManyHostsResponseDto",
    "SetPortToManyHostsResponseDto",
    "SetPortToManyHostsRequestDto",
    # Users models
    "CreateUserRequestDto",
    "UpdateUserRequestDto",
    "RevokeUserRequestDto",
    "CreateUserResponseDto",
    "UpdateUserResponseDto",
    "GetUserByUuidResponseDto",
    "GetUserByShortUuidResponseDto",
    "GetUserByUsernameResponseDto",
    "GetUserByIdResponseDto",
    "DisableUserResponseDto",
    "EnableUserResponseDto",
    "ResetUserTrafficResponseDto",
    "RevokeUserSubscriptionResponseDto",
    "ActivateAllInboundsResponseDto",
    "GetAllUsersResponseDto",
    "GetAllTagsResponseDto",
    "GetUserSubscriptionRequestHistoryResponseDto",
    "TelegramUserResponseDto",
    "EmailUserResponseDto",
    "TagUserResponseDto",
    "DeleteUserResponseDto",
    "UserResponseDto",
    "UsersResponseDto",
    "TagsResponseDto",
    "SubscriptionRequestsResponseData",
    "UserTrafficDto",
    "ActiveInternalSquadDto",
    "SubscriptionRequestRecord",
    "HappCrypto",
    "UserActiveInboundsDto",
    "UserLastConnectedNodeDto",
    "GetSubscriptionRequestsResponseDto",
    # Users bulk actions models
    "BulkAllExtendExpirationDateRequestDto",
    "BulkAllExtendExpirationDateResponseDto",
    "BulkAllResetTrafficUsersResponseDto",
    "BulkAllUpdateUsersRequestDto",
    "BulkAllUpdateUsersResponseDto",
    "BulkDeleteUsersByStatusRequestDto",
    "BulkDeleteUsersByStatusResponseDto",
    "BulkDeleteUsersRequestDto",
    "BulkDeleteUsersResponseDto",
    "BulkEventResponseData",
    "BulkExtendExpirationDateRequestDto",
    "BulkExtendExpirationDateResponseDto",
    "BulkResetTrafficUsersRequestDto",
    "BulkResetTrafficUsersResponseDto",
    "BulkResponseData",
    "BulkResponseDto",
    "BulkRevokeUsersSubscriptionRequestDto",
    "BulkRevokeUsersSubscriptionResponseDto",
    "BulkUpdateUsersInternalSquadsRequestDto",
    "BulkUpdateUsersRequestDto",
    "BulkUpdateUsersResponseDto",
    "BulkUpdateUsersSquadsRequestDto",
    "BulkUpdateUsersSquadsResponseDto",
    "TagStr",
    "UpdateUserFields",
    # Users stats models
    "UserUsageByRange",
    "UserUsageByRangeResponseDto",
    # Config profiles models
    "ConfigProfileDto",
    "CreateConfigProfileRequestDto",
    "CreateConfigProfileResponseDto",
    "DeleteConfigProfileResponseDto",
    "GetAllConfigProfilesResponseDto",
    "GetAllInboundsResponseDto",
    "GetConfigProfileByUuidResponseDto",
    "GetInboundsByProfileUuidResponseDto",
    "InboundDto",
    "NodesProfileDto",
    "UpdateConfigProfileRequestDto",
    "UpdateConfigProfileResponseDto",
    "GetAllConfigProfilesResponsePaginated",
    # Infra billing models
    "CreateInfraBillingHistoryRecordRequestDto",
    "CreateInfraBillingHistoryRecordResponseDto", 
    "CreateInfraBillingNodeRequestDto",
    "CreateInfraBillingNodeResponseDto",
    "CreateInfraProviderRequestDto",
    "CreateInfraProviderResponseDto",   
    "DeleteInfraBillingHistoryRecordByUuidResponseDto",  
    "DeleteInfraBillingNodeByUuidResponseDto",  # ПЕРЕИМЕНОВАНА (было DeleteInfraBillingNodeResponseDto)
    "DeleteInfraProviderByUuidResponseDto",  # ПЕРЕИМЕНОВАНА (было DeleteInfraProviderResponseDto)
    "GetInfraBillingHistoryRecordsResponseDto",  # ПЕРЕИМЕНОВАНА (было GetAllInfraBillingHistoryResponseDto)
    "GetInfraBillingNodesResponseDto",  # ПЕРЕИМЕНОВАНА (было GetAllInfraBillingNodesResponseDto)
    "GetInfraProvidersResponseDto",  # ПЕРЕИМЕНОВАНА (было GetAllInfraProvidersResponseDto)
    "GetInfraBillingHistoryByUuidResponseDto",
    "GetInfraBillingNodeByUuidResponseDto",
    "GetInfraProviderByUuidResponseDto",
    "InfraBillingHistoryDto",
    "InfraBillingNodeDto",
    "InfraProviderDto",
    "NodeDto",
    "UpdateInfraBillingNodeRequestDto",
    "UpdateInfraBillingNodeResponseDto",
    "UpdateInfraProviderRequestDto",
    "UpdateInfraProviderResponseDto",
    "DeleteInfraBillingNodeResponseDto",  # LEGACY
    "DeleteInfraProviderResponseDto",  # LEGACY
    "GetAllInfraBillingHistoryResponseDto",  # LEGACY
    "GetAllInfraBillingNodesResponseDto",  # LEGACY
    "GetAllInfraProvidersResponseDto",  # LEGACY
    # Internal squads models
    "AddUsersToInternalSquadRequestDto",
    "AddUsersToInternalSquadResponseDto",
    "CreateInternalSquadRequestDto",
    "CreateInternalSquadResponseDto",
    "DeleteInternalSquadResponseDto",
    "DeleteUsersFromInternalSquadRequestDto",
    "DeleteUsersFromInternalSquadResponseDto",
    "GetAllInternalSquadsResponseDto",
    "GetInternalSquadByUuidResponseDto",
    "InternalSquadDto",
    "UpdateInternalSquadRequestDto",
    "UpdateInternalSquadResponseDto",
    # Nodes usage history models
    "GetNodeUserUsageByRangeResponseDto",
    "GetNodesUsageByRangeResponseDto",
    "GetUserAccessibleNodesResponseDto",
    "NodeInfoDto",
    "NodeUsageDto",
    "UserUsageDto",
    # Subscription request history models
    "GetAllSubscriptionRequestHistoryResponseDto",
    "GetSubscriptionRequestHistoryStatsResponseDto",
    "SubscriptionRequestHistoryRecord",
    "SubscriptionRequestHistoryData",
    "AppStatItem",
    "HourlyRequestStat", 
    "SubscriptionRequestHistoryStatsData",
    # Webhook models
     # USER
    "LastConnectedNodeDto",
    "InternalSquadDto",
    "BaseUserDto",
    "UserDto",
    "UserEventDto",
    "UserTrafficDto",

    # HWID DEVICES
    "HwidUserDeviceDto",
    "UserHwidDeviceEventDto",

    # SERVICE EVENTS
    "LoginAttemptDto",
    "ServiceEventDto",

    # NODE ENTITIES
    "ConfigProfileInboundDto",
    "InfraProviderDto",
    "NodeDto",
    "NodeEventDto",

    # ERROR EVENTS
    "CustomErrorEventDto",

    # CRM EVENTS
    "CrmEventDto",

    # WEBHOOK PAYLOAD
    "WebhookPayloadDto",
    
    # Passkeys models
    "DeletePasskeyRequestDto",
    "DeletePasskeyResponseDto",
    "GetAllPasskeysResponseDto",
    "GetPasskeyRegistrationOptionsResponseDto",
    "PasskeyDto",
    "VerifyPasskeyRegistrationRequestDto",
    "VerifyPasskeyRegistrationResponseDto",
    
    # External squads models
    "AddUsersToExternalSquadResponseDto",
    "CreateExternalSquadRequestDto",
    "CreateExternalSquadResponseDto",
    "DeleteExternalSquadResponseDto",
    "ExternalSquadDto",
    "ExternalSquadInfoDto",
    "ExternalSquadSubscriptionSettingsDto",
    "ExternalSquadTemplateDto",
    "GetExternalSquadByUuidResponseDto",
    "GetExternalSquadsResponseDto",
    "RemoveUsersFromExternalSquadResponseDto",
    "TemplateType",
    "UpdateExternalSquadRequestDto",
    "UpdateExternalSquadResponseDto",
    
    # Snippets models

    "CreateSnippetRequestDto",
    "CreateSnippetResponseDto",
    "DeleteSnippetRequestDto",
    "DeleteSnippetResponseDto",
    "GetSnippetsResponseDto",
    "SnippetItem",
    "SnippetsData",
    "UpdateSnippetRequestDto",
    "UpdateSnippetResponseDto",
    
    # Remnawave settings models
    
    "BrandingSettings",
    "GetRemnawaveSettingsResponseDto",
    "GitHubOAuth2Settings",
    "OAuth2Settings",
    "PasskeySettings",
    "PasswordSettings",
    "PocketIdOAuth2Settings",
    "RemnawaveSettingsData",
    "TelegramAuthSettings",
    "UpdateRemnawaveSettingsRequestDto",
    "UpdateRemnawaveSettingsResponseDto",
    "YandexOAuth2Settings",
    
    # Subscription page config models
    "CloneSubscriptionPageConfigRequestDto",
    "CloneSubscriptionPageConfigResponseDto",
    "CreateSubscriptionPageConfigRequestDto",
    "CreateSubscriptionPageConfigResponseDto",
    "DeleteSubscriptionPageConfigResponseDto",
    "GetSubscriptionPageConfigResponseDto",
    "GetSubscriptionPageConfigsResponseDto",
    "ReorderSubscriptionPageConfigItem",
    "ReorderSubscriptionPageConfigsRequestDto",
    "ReorderSubscriptionPageConfigsResponseDto",
    "SubscriptionPageConfigDto",
    "UpdateSubscriptionPageConfigRequestDto",
    "UpdateSubscriptionPageConfigResponseDto",
]
