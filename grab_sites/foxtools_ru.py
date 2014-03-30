import requests
from proxy_utils import parse_proxy


def grab_proxies():
    proxies = []
    for i in range(1, 6):
        print('[i]->Foxtools.ru page: {}'.format(i))
        response = requests.get("http://foxtools.ru/Proxy?page={}".format(str(i)))
        proxies += parse_proxy(response.text)
    return proxies