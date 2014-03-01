import requests
from proxy_utils import parse_proxy


def grab_page(num_page):
    response = requests.get("http://foxtools.ru/Proxy?page={}".format(str(num_page)))
    return parse_proxy(response.text)


def grab_proxies():
    proxies = []

    for i in range(1, 6):
        print('[i]->Foxtools.ru page: {}'.format(i))
        proxies += grab_page(i)
    return proxies