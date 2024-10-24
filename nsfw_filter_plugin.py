from typing import Optional

from proxy.http.proxy import HttpProxyBasePlugin
from proxy.http.parser import HttpParser

from constants.blacklist import blacklist
import re

class NsfwFilterPlugin(HttpProxyBasePlugin):
    """Modifies upstream server responses."""

    def handle_client_request(self, request: HttpParser) -> Optional[HttpParser]:
        urlProtocolRegExp = "(https|http)?(://)?(www\\.)?[/]*"
        referer_header = request.headers.get(b'referer')
        referer_url = None

        if (referer_header is not None):
            referer_url = re.sub(urlProtocolRegExp, "", referer_header[1].decode('utf-8'))

        site_url = re.sub(urlProtocolRegExp, "", (request.host or b'').decode("utf-8"))

        request.add_header(key=b'x-blacklisted-site', value=str(site_url in blacklist or ((referer_url is not None) and referer_url in blacklist)).encode('ASCII'))
        
        return request
