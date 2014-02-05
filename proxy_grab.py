from grab_sites import hideme_ru, samair_ru, gatherproxy_com

proxies = []


result = hideme_ru.grab()
proxies += result
result = samair_ru.grab()
proxies += result
result = gatherproxy_com.grab()
proxies += result

with open('source.txt', 'a') as f:
    f.write('\n'.join(proxies))