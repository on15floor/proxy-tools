import requests
from proxy_utils import parse_proxy


def grab_proxies():
    return parse_proxy(requests.get("http://www.prime-speed.ru/proxy/free-proxy-list/all-working-proxies.php").text)