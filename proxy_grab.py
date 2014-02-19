from grab_sites import gatherproxy_com, shroomery_org, hideme_ru, samair_ru, freeproxy_ch, proxy_list_org, \
    proxylife_org, fineproxy_org, xroxy_com, seprox_ru, therealist_ru, nntime_com
from proxy_utils import write_proxies
from utils import notify

proxies = []

functions = [
    hideme_ru.grab_proxies,
    samair_ru.grab_proxies,
    gatherproxy_com.grab_proxies,
    shroomery_org.grab_proxies,
    freeproxy_ch.grab_proxies,
    proxy_list_org.grab_proxies,
    proxylife_org.grab_proxies,
    fineproxy_org.grab_proxies,
    xroxy_com.grab_proxies,
    seprox_ru.grab_proxies,
    therealist_ru.grab_proxies,
    nntime_com.grab_proxies,
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
notify('[{}] Finished'.format(__file__))