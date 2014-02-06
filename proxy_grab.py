from grab_sites import hideme_ru, samair_ru, gatherproxy_com
from proxy_utils import write_proxies

proxies = []

functions = [
    hideme_ru.grab_proxies,
    samair_ru.grab_proxies,
    gatherproxy_com.grab_proxies
]

for func in functions:
    result = None
    try:
        result = func()
        if result:
            proxies += result
    except Exception as e:
        print(e)

write_proxies('source.txt', proxies)