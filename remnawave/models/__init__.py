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
    CreateInfraBillingNodeRequestDto,
    CreateInfraBillingNodeResponseDto,
    CreateInfraProviderRequestDto,
    CreateInfraProviderResponseDto,
    DeleteInfraBillingNodeResponseDto,
    DeleteInfraProviderResponseDto,
    GetAllInfraBillingHistoryResponseDto,
    GetAllInfraBillingNodesResponseDto,
    GetAllInfraProvidersResponseDto,
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
)
from .subscriptions_settings import (
    GetSubscriptionSettingsResponseDto,
    SubscriptionSettingsResponseDto,
    UpdateSubscriptionSettingsRequestDto,
    UpdateSubscriptionSettingsResponseDto,
)
from .subscriptions_template import (
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
)
from .users import (
    ActiveInternalSquadDto,
    CreateUserRequestDto,
    DeleteUserResponseDto,
    EmailUserResponseDto,
    TelegramUserResponseDto,
    UpdateUserRequestDto,
    UserActiveInboundsDto,
    UserLastConnectedNodeDto,
    UserResponseDto,
    UsersResponseDto,
    TagsResponseDto,
    RevokeUserRequestDto,
)
from .users_bulk_actions import (
    BulkAllResetTrafficUsersResponseDto,
    BulkAllUpdateUsersRequestDto,
    BulkAllUpdateUsersResponseDto,
    BulkResponseDto,
    BulkUpdateUsersInboundsRequestDto,
    UpdateUserFields,
)
from .users_stats import UserUsageByRange, UserUsageByRangeResponseDto
from .xray_config import (
    ConfigResponseDto,  # Legacy alias
    GetConfigResponseDto,
    UpdateConfigRequestDto,
    UpdateConfigResponseDto,
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
    # Inbounds models
    "FullInboundResponseDto",
    "FullInboundStatistic",
    "FullInboundsResponseDto",
    "GetFullInboundsResponseDto",
    "GetInboundsResponseDto",
    "InboundResponseDto",
    "InboundsResponseDto",  # Legacy alias
    "GetInternalSquadAccessibleNodesResponseDto",
    # Keygen models
    "GetPubKeyResponseDto",
    "PubKeyResponseDto",  # Legacy alias
    # Subscription models
    "GetAllSubscriptionsResponseDto",
    "GetSubscriptionByUsernameResponseDto",
    "GetSubscriptionInfoResponseDto",
    "SubscriptionInfoResponseDto",  # Legacy alias
    "UserSubscription",
    # Subscription settings models
    "GetSubscriptionSettingsResponseDto",
    "SubscriptionSettingsResponseDto",
    "UpdateSubscriptionSettingsRequestDto",
    "UpdateSubscriptionSettingsResponseDto",
    # Subscription template models
    "GetTemplateResponseDto",
    "TemplateResponseDto",
    "UpdateTemplateRequestDto",
    "UpdateTemplateResponseDto",
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
    # Bandwidth stats models
    "GetNodeUserUsageByRangeResponseDto",
    "GetNodesRealtimeUsageResponseDto",
    "GetNodesUsageByRangeResponseDto",
    "GetUserUsageByRangeResponseDto",
    "NodeRealtimeUsageResponseDto",
    "NodeUsageResponseDto",
    "NodesRealtimeUsageResponseDto",  # Legacy alias
    "NodesUsageResponseDto",  # Legacy alias
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
    # Users models
    "ActiveInternalSquadDto",
    "CreateUserRequestDto",
    "CreateUserResponseDto",
    "DeleteUserResponseDto",
    "DisableUserResponseDto",
    "EmailUserResponseDto",
    "EnableUserResponseDto",
    "GetAllUsersResponseDto",
    "GetUserByEmailResponseDto",
    "GetUserByShortUuidResponseDto",
    "GetUserBySubscriptionUuidResponseDto",
    "GetUserByTagResponseDto",
    "GetUserByTelegramIdResponseDto",
    "GetUserByUsernameResponseDto",
    "GetUserByUuidResponseDto",
    "ResetUserTrafficResponseDto",
    "RevokeUserRequestDto",
    "RevokeUserSubscriptionResponseDto",
    "TagsResponseDto",
    "TelegramUserResponseDto",
    "UpdateUserRequestDto",
    "UpdateUserResponseDto",
    "UserActiveInboundsDto",
    "UserLastConnectedNodeDto",
    "UserResponseDto",
    "UsersResponseDto",
    # Users bulk actions models
    "BulkAllResetTrafficUsersResponseDto",
    "BulkAllUpdateUsersRequestDto",
    "BulkAllUpdateUsersResponseDto",
    "BulkResponseDto",
    "BulkUpdateUsersInboundsRequestDto",
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
    "UpdateConfigProfileRequestDto",
    "UpdateConfigProfileResponseDto",
    # Infra billing models
    "CreateInfraBillingNodeRequestDto",
    "CreateInfraBillingNodeResponseDto",
    "CreateInfraProviderRequestDto",
    "CreateInfraProviderResponseDto",
    "DeleteInfraBillingNodeResponseDto",
    "DeleteInfraProviderResponseDto",
    "GetAllInfraBillingHistoryResponseDto",
    "GetAllInfraBillingNodesResponseDto",
    "GetAllInfraProvidersResponseDto",
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
]
