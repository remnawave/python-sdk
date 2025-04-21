from enum import StrEnum


class ALPN(StrEnum):
    H3 = "h3"
    H2 = "h2"
    HTTP_1_1 = "http/1.1"
    H_COMBINED = "h2,http/1.1"
    H3_H2_H1_COMBINED = "h3,h2,http/1.1"
    H3_H2_COMBINED = "h3,h2"
