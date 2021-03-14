from proxy_utils import *
from utils import *
from proxy_utils import read_proxies


def proxy_check(file_name: str, proxy_type: str):
    proxies = read_proxies(file_name)
    proxy_manager = ProxyManager(proxy_type)
    proxy_good = []

    for proxy in proxy_manager.check_anonymity_parallel(proxies, 10):
        proxy_good.append(proxy)

    write_list_w('proxy_{}.txt'.format(proxy_type), proxy_good)
