import requests
from proxy_utils import parse_proxy


def grab_proxies():
    return parse_proxy(requests.get('http://www.shroomery.org/ythan/proxylist.php').text)