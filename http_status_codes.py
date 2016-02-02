# coding=utf-8

from collections import namedtuple

HTTPStatusCodeCategory = namedtuple('StatusCodeCategory', 'code, name, description')

http_status_code_category = [
    HTTPStatusCodeCategory('1xx', 'Informational', 'Request received, continuing process'),
    HTTPStatusCodeCategory('2xx', 'Success', 'The action was successfully received, understood, and accepted'),
    HTTPStatusCodeCategory('3xx', 'Redirection', 'Further action must be taken in order to complete the request'),
    HTTPStatusCodeCategory('4xx', 'Client Error', 'The request contains bad syntax or cannot be fulfilled'),
    HTTPStatusCodeCategory('5xx', 'Server Error', 'The server failed to fulfill an apparently valid request'),                           
]


HTTPStatusCode = namedtuple('StatusCode', ['code, name, description'])

http_status_code_category = [
    HTTPStatusCode(100, 'Continue', '[RFC7231, Section 6.2.1]'),
    HTTPStatusCode(101, 'Switching Protocols', '[RFC7231, Section 6.2.2]'),
    HTTPStatusCode(102, 'Processing', '[RFC2518]'),
    HTTPStatusCode(200, 'OK', '[RFC7231, Section 6.3.1]'),
    HTTPStatusCode(201, 'Created', '[RFC7231, Section 6.3.2]'),
    HTTPStatusCode(202, 'Accepted', '[RFC7231, Section 6.3.3]'),
    HTTPStatusCode(203, 'Non-Authoritative Information', '[RFC7231, Section 6.3.4]'),
    HTTPStatusCode(204, 'No Content', '[RFC7231, Section 6.3.5]'),
    HTTPStatusCode(205, 'Reset Content', '[RFC7231, Section 6.3.6]'),
    HTTPStatusCode(206, 'Partial Content', '[RFC7233, Section 4.1]'),
    HTTPStatusCode(207, 'Multi-Status', '[RFC4918]'),
    HTTPStatusCode(208, 'Already Reported', '[RFC5842]'),
    HTTPStatusCode(226, 'IM Used', '[RFC3229]'),
    HTTPStatusCode(300, 'Multiple Choices', '[RFC7231, Section 6.4.1]'),
    HTTPStatusCode(301, 'Moved Permanently', '[RFC7231, Section 6.4.2]'),
    HTTPStatusCode(302, 'Found', '[RFC7231, Section 6.4.3]'),
    HTTPStatusCode(303, 'See Other', '[RFC7231, Section 6.4.4]'),
    HTTPStatusCode(304, 'Not Modified', '[RFC7232, Section 4.1]'),
    HTTPStatusCode(305, 'Use Proxy', '[RFC7231, Section 6.4.5]'),
    HTTPStatusCode(306, '(Unused)', '[RFC7231, Section 6.4.6]'),
    HTTPStatusCode(307, 'Temporary Redirect', '[RFC7231, Section 6.4.7]'),
    HTTPStatusCode(308, 'Permanent Redirect', '[RFC7538]'),
    HTTPStatusCode(400, 'Bad Request', '[RFC7231, Section 6.5.1]'),
    HTTPStatusCode(401, 'Unauthorized', '[RFC7235, Section 3.1]'),
    HTTPStatusCode(402, 'Payment Required', '[RFC7231, Section 6.5.2]'),
    HTTPStatusCode(403, 'Forbidden', '[RFC7231, Section 6.5.3]'),
    HTTPStatusCode(404, 'Not Found', '[RFC7231, Section 6.5.4]'),
    HTTPStatusCode(405, 'Method Not Allowed', '[RFC7231, Section 6.5.5]'),
    HTTPStatusCode(406, 'Not Acceptable', '[RFC7231, Section 6.5.6]'),
    HTTPStatusCode(407, 'Proxy Authentication Required', '[RFC7235, Section 3.2]'),
    HTTPStatusCode(408, 'Request Timeout', '[RFC7231, Section 6.5.7]'),
    HTTPStatusCode(409, 'Conflict', '[RFC7231, Section 6.5.8]'),
    HTTPStatusCode(410, 'Gone', '[RFC7231, Section 6.5.9]'),
    HTTPStatusCode(411, 'Length Required', '[RFC7231, Section 6.5.10]'),
    HTTPStatusCode(412, 'Precondition Failed', '[RFC7232, Section 4.2]'),
    HTTPStatusCode(413, 'Payload Too Large', '[RFC7231, Section 6.5.11]'),
    HTTPStatusCode(414, 'URI Too Long', '[RFC7231, Section 6.5.12]'),
    HTTPStatusCode(415, 'Unsupported Media Type', '[RFC7231, Section 6.5.13], [RFC7694, Section 3]'),
    HTTPStatusCode(416, 'Range Not Satisfiable', '[RFC7233, Section 4.4]'),
    HTTPStatusCode(417, 'Expectation Failed', '[RFC7231, Section 6.5.14]'),
    HTTPStatusCode(421, 'Misdirected Request', '[RFC7540, Section 9.1.2]'),
    HTTPStatusCode(422, 'Unprocessable Entity', '[RFC4918]'),
    HTTPStatusCode(423, 'Locked', '[RFC4918]'),
    HTTPStatusCode(424, 'Failed Dependency', '[RFC4918]'),
    HTTPStatusCode(426, 'Upgrade Required', '[RFC7231, Section 6.5.15]'),
    HTTPStatusCode(428, 'Precondition Required', '[RFC6585]'),
    HTTPStatusCode(429, 'Too Many Requests', '[RFC6585]'),
    HTTPStatusCode(431, 'Request Header Fields Too Large', '[RFC6585]'),
    HTTPStatusCode(451, 'Unavailable for Legal Reasons', '[RFC-ietf-httpbis-legally-restricted-status-04]'),
    HTTPStatusCode(500, 'Internal Server Error', '[RFC7231, Section 6.6.1]'),
    HTTPStatusCode(501, 'Not Implemented', '[RFC7231, Section 6.6.2]'),
    HTTPStatusCode(502, 'Bad Gateway', '[RFC7231, Section 6.6.3]'),
    HTTPStatusCode(503, 'Service Unavailable', '[RFC7231, Section 6.6.4]'),
    HTTPStatusCode(504, 'Gateway Timeout', '[RFC7231, Section 6.6.5]'),
    HTTPStatusCode(505, 'HTTP Version Not Supported', '[RFC7231, Section 6.6.6]'),
    HTTPStatusCode(506, 'Variant Also Negotiates', '[RFC2295]'),
    HTTPStatusCode(507, 'Insufficient Storage', '[RFC4918]'),
    HTTPStatusCode(508, 'Loop Detected', '[RFC5842]'),
    HTTPStatusCode(510, 'Not Extended', '[RFC2774]'),
    HTTPStatusCode(511, 'Network Authentication Required', '[RFC6585]'),
]