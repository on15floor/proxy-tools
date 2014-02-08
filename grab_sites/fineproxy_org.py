import requests
from proxy_utils import parse_proxy


def grab_proxies():
    return parse_proxy(requests.get("http://fineproxy.org/%D1%81%D0%B2%D0%B5%D0%B6%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%BA%D1%81%D0%B8/").text)