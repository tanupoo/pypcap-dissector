# common keys
JK_PROTO = "PROTO"
JK_HEADER = "HEADER"
JK_PAYLOAD = "PAYLOAD"
JK_EMSG = "EMSG"

# keys for field/attribute name
JK_EN10MB = "EN10MB"
JK_EN10MB_DMAC = JK_EN10MB + ".DMAC"
JK_EN10MB_SMAC = JK_EN10MB + ".SMAC"
JK_EN10MB_TYPE = JK_EN10MB + ".TYPE"

JK_DLT_NULL = "DLT_NULL"
JK_DLT_NULL_AF = JK_DLT_NULL + ".AF"

JK_IPV6 = "IPV6"
JK_IPV6_VER = JK_IPV6 + ".VER"
JK_IPV6_TC = JK_IPV6 + ".TC"
JK_IPV6_FL = JK_IPV6 + ".FL"
JK_IPV6_LEN = JK_IPV6 + ".LEN"
JK_IPV6_NXT = JK_IPV6 + ".NXT"
JK_IPV6_HOP_LMT = JK_IPV6 + ".HOP_LMT"
JK_IPV6_SADDR = JK_IPV6 + ".SADDR"
JK_IPV6_DADDR = JK_IPV6 + ".DADDR"

JK_ICMPV6 = "ICMPV6"
JK_ICMPV6_TYPE = JK_ICMPV6 + ".TYPE"
JK_ICMPV6_CODE = JK_ICMPV6 + ".CODE"
JK_ICMPV6_CKSUM = JK_ICMPV6 + ".CKSUM"

JK_IPV4 = "IPV4"
JK_IPV4_TOS = JK_IPV4 + ".TOS"
JK_IPV4_LEN = JK_IPV4 + ".LEN"
JK_IPV4_IDENT = JK_IPV4 + ".IDENT"
JK_IPV4_TTL = JK_IPV4 + ".TTL"
JK_IPV4_NXT = JK_IPV4 + ".NXT"
JK_IPV4_CKSUM = JK_IPV4 + ".CKSUM"
JK_IPV4_SADDR = JK_IPV4 + ".SADDR"
JK_IPV4_DADDR = JK_IPV4 + ".DADDR"
JK_IPV4_VER = JK_IPV4 + ".VER"
JK_IPV4_HDR_LEN = JK_IPV4 + ".HDR_LEN"
JK_IPV4_FLAG = JK_IPV4 + ".FLAG"
JK_IPV4_OFFSET = JK_IPV4 + ".OFFSET"

JK_UDP = "UDP"
JK_UDP_SPORT = JK_UDP + ".SPORT"
JK_UDP_DPORT = JK_UDP + ".DPORT"
JK_UDP_LEN = JK_UDP + ".LEN"
JK_UDP_CKSUM = JK_UDP + ".CKSUM"

JK_COAP = "COAP"
JK_COAP_CODE = JK_COAP + ".CODE"
JK_COAP_MSGID = JK_COAP + ".MSGID"
JK_COAP_VER = JK_COAP + ".VER"
JK_COAP_TYPE = JK_COAP + ".TYPE"
JK_COAP_TOKEN_LEN = JK_COAP + ".TOKEN_LEN"
JK_COAP_TOKEN = JK_COAP + ".TOKEN"
