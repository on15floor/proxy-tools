import requests
from proxy_utils import parse_proxy


def grab_proxies():
    proxies = []
    for i in range(0, 2):
        print('[i]->Speedtest.at page: {}'.format(i))
        response = requests.get("http://proxy.speedtest.at/proxybyActuality.php?offset={}".format(i * 25))
        proxies += parse_proxy(response.text)
    return proxies