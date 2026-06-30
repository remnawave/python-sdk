from enum import StrEnum


class MihomoIpVersion(StrEnum):
    DUAL = "dual"
    IPV4 = "ipv4"
    IPV6 = "ipv6"
    IPV4_PREFER = "ipv4-prefer"
    IPV6_PREFER = "ipv6-prefer"
