import requests
from proxy_utils import parse_proxies


def grab_proxies(number_of_page=6):
    proxies = []
    for i in range(1, number_of_page):
        print('[i]->Foxtools.ru page: {}'.format(i))
        response = requests.get(f"http://foxtools.ru/Proxy?page={str(i)}")
        proxies += parse_proxies(response.text)
    return proxies