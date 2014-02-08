from grab_sites import gatherproxy_com, shroomery_org, hideme_ru, samair_ru
from proxy_utils import write_proxies

proxies = []

functions = [
    hideme_ru.grab_proxies,
    samair_ru.grab_proxies,
    gatherproxy_com.grab_proxies,
    shroomery_org.grab_proxies
]

for func in functions:
    result = None
    print('[i]Site:' + func.__module__)
    try:
        result = func()
        if result:
            proxies += result
            print('[+]Proxy from site:' + str(len(result)).zfill(5) + ', Total:' + str(len(proxies)).zfill(5))
    except Exception as e:
        print(e)

write_proxies('source.txt', proxies)