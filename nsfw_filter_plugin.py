from typing import Optional

from proxy.http.proxy import HttpProxyBasePlugin
from proxy.http.parser import HttpParser, httpParserTypes
from proxy.http.codes import httpStatusCodes
from proxy.common.utils import build_http_response
from utils.get_random_image import getRandomImage
from proxy.http.responses import okResponse
from proxy.common.constants import HTTP_1_1

from constants.blacklist import blacklist
import re

class NsfwFilterPlugin(HttpProxyBasePlugin):
    """Modifies upstream server responses."""

    def __init__(self, *args: any, **kwargs: any) -> None:
        super().__init__(*args, **kwargs)
        # Create a new http protocol parser for response payloads
        self.response = HttpParser(httpParserTypes.RESPONSE_PARSER)

    def handle_client_request(self, request: HttpParser) -> Optional[HttpParser]:
        urlProtocolRegExp = "(https|http)?(://)?(www\\.)?[/]*"
        referer_header = request.headers.get(b'referer')
        referer_url = None

        if (referer_header is not None):
            referer_url = re.sub(urlProtocolRegExp, "", referer_header[1].decode('utf-8'))

        site_url_header = request.headers.get(b'host')
        site_url = re.sub(urlProtocolRegExp, "", (request.host or (site_url_header is not None and site_url_header[1]) or b'').decode('utf-8'))

        request.add_header(key=b'x-blacklisted-site', value=str(site_url in blacklist or ((referer_url is not None) and referer_url in blacklist)).encode('ASCII'))

        self.local_request = request
        
        if (request.headers.get(b'x-blacklisted-site')[1] == b'True'): print("Blacklisted: ", site_url)

        return request

    def handle_upstream_chunk(self, chunk: memoryview) -> Optional[memoryview]:
        self.response.parse(chunk)
        if (self.local_request is not None):
            content_type_header = self.response.headers.get(b'content-type')
            black_listed_header = self.local_request.headers.get(b'x-blacklisted-site')

            content_type = content_type_header[1].decode('utf-8') if content_type_header is not None else ""
            black_listed = black_listed_header[1] == b'True' if black_listed_header is not None else False

            if (content_type.startswith("video")):
                if (black_listed):
                    safe_response = HttpParser(httpParserTypes.RESPONSE_PARSER)
                    safe_response.code = str(httpStatusCodes.FORBIDDEN).encode('utf-8')
                    safe_response.reason = b'Blocked by NSFW Proxy BlackList'
                    safe_response.version = HTTP_1_1
                    
                    return memoryview(safe_response.build_response());

            if (content_type.startswith("image")):
                if (black_listed):
                    safe_response = HttpParser(httpParserTypes.RESPONSE_PARSER)
                    safe_response.code = str(httpStatusCodes.FORBIDDEN).encode('utf-8')
                    safe_response.reason = b'Blocked by NSFW Proxy BlackList'
                    safe_response.version = HTTP_1_1
                    safe_response.body = getRandomImage();
                    
                    return memoryview(safe_response.build_response());

        return chunk
