import requests
from grab_sites import nntime_com, ip_adress_com, echolink_org, foxtools_ru
from proxy_utils import parse_proxies
from utils import read_list, SilentException

proxy_count = 0


def full_grab():
    global proxy_count
    proxies = []
    functions = [nntime_com.grab_proxies, ip_adress_com.grab_proxies, echolink_org.grab_proxies,
                 foxtools_ru.grab_proxies]
    for func in functions:
        print(f'[i]Site:{func.__module__}')
        try:
            result_func = func()
            if result_func:
                proxies += result_func
                proxy_count += len(result_func)
                print(f'[+]Proxy from site:{str(len(result_func)).zfill(5)}, Total:{str(proxy_count).zfill(5)}')
            else:
                print(f'[-]No proxy from:{func.__module__}')
        except SilentException as e:
            print(e)
    proxies += fast_grab()
    return proxies


def fast_grab():
    global proxy_count
    proxies = []
    sites = read_list('sites.txt')

    for site in sites:
        print(f'[i]Site:{site}')
        try:
            proxies_from_site = parse_proxies(requests.get(site).text)
            if len(proxies_from_site) != 0:
                proxies += proxies_from_site
                proxy_count += len(proxies_from_site)
                print(f'[+]Proxy from site:{str(len(proxies_from_site)).zfill(5)}, Total:{str(proxy_count).zfill(5)}')
            else:
                print(f'[-]No proxy from: {site}')
        except SilentException as e:
            print(f'[-]Dead Site: {site}', e)

    return proxies
