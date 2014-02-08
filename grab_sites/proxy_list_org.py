import requests
from proxy_utils import parse_proxy


def grab_proxies():
    proxies = []

    for i in range(1, 11):
        print('[i]->Proxy-list.org page: {}'.format(i))
        page = str(i).zfill(2)
        response = requests.get("http://proxy-list.org/russian/index.php?p={}".format(page))
        proxies += parse_proxy(response.text)

    return proxies